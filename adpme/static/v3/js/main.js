/* ==========================================================================
   ADPME Congo — main.js — v2
   JavaScript maison, sans dépendance. Chaque fonction s'active seulement si
   l'élément HTML correspondant (attribut data-…) est présent sur la page.
   ========================================================================== */
(function () {
  "use strict";

  var ORDINATEUR = window.matchMedia("(min-width: 1100px)");

  /* ── Fermer un message (alerte Django) ─────────────────────────────── */
  function initAlertes() {
    document.querySelectorAll("[data-alerte-fermer]").forEach(function (bouton) {
      bouton.addEventListener("click", function () {
        var alerte = bouton.closest("[data-alerte]");
        if (alerte) alerte.remove();
      });
    });
  }

  /* ── Défilement : ombre de l'en-tête + bouton « retour en haut » ───── */
  function initDefilement() {
    var header = document.querySelector("[data-header]");
    var bouton = document.querySelector("[data-retour-haut]");
    if (!header && !bouton) return;

    var enAttente = false;
    function maj() {
      var y = window.scrollY;
      if (header) header.classList.toggle("est-defile", y > 40);
      if (bouton) bouton.classList.toggle("est-visible", y > 600);
      enAttente = false;
    }
    window.addEventListener("scroll", function () {
      if (!enAttente) {
        enAttente = true;
        window.requestAnimationFrame(maj);
      }
    }, { passive: true });

    if (bouton) {
      bouton.addEventListener("click", function () {
        window.scrollTo({ top: 0 });
        var contenu = document.getElementById("contenu");
        if (contenu) contenu.focus({ preventScroll: true });
      });
    }
    maj();
  }

  /* ── En-tête : méga-menu, menu mobile, recherche ───────────────────── */
  function initEntete() {
    var header = document.querySelector("[data-header]");
    if (!header) return;

    var burger = header.querySelector("[data-burger]");
    var boutonsMega = Array.prototype.slice.call(header.querySelectorAll("[data-mega-bouton]"));
    var boutonRecherche = header.querySelector("[data-recherche-bouton]");
    var panneauRecherche = boutonRecherche && document.getElementById(boutonRecherche.getAttribute("aria-controls"));

    function panneauDe(bouton) {
      return document.getElementById(bouton.getAttribute("aria-controls"));
    }

    /* Méga-menus */
    function fermerMegas(sauf) {
      boutonsMega.forEach(function (b) {
        if (b === sauf) return;
        b.setAttribute("aria-expanded", "false");
        panneauDe(b).hidden = true;
      });
    }
    function megaOuvert() {
      for (var i = 0; i < boutonsMega.length; i++) {
        if (boutonsMega[i].getAttribute("aria-expanded") === "true") return boutonsMega[i];
      }
      return null;
    }
    boutonsMega.forEach(function (bouton) {
      bouton.addEventListener("click", function () {
        var ouvrir = bouton.getAttribute("aria-expanded") !== "true";
        if (ORDINATEUR.matches) fermerMegas(bouton);
        if (ouvrir && ORDINATEUR.matches) fermerRecherche();
        bouton.setAttribute("aria-expanded", String(ouvrir));
        panneauDe(bouton).hidden = !ouvrir;
      });
    });

    /* Menu mobile */
    function menuOuvert() {
      return burger && burger.getAttribute("aria-expanded") === "true";
    }
    function ouvrirMenu() {
      fermerRecherche();
      header.style.setProperty("--nav-top", header.getBoundingClientRect().bottom + "px");
      header.classList.add("menu-ouvert");
      document.body.classList.add("menu-ouvert");
      burger.setAttribute("aria-expanded", "true");
    }
    function fermerMenu() {
      if (!burger) return;
      header.classList.remove("menu-ouvert");
      document.body.classList.remove("menu-ouvert");
      burger.setAttribute("aria-expanded", "false");
      fermerMegas();
    }
    if (burger) {
      burger.addEventListener("click", function () {
        if (menuOuvert()) { fermerMenu(); } else { ouvrirMenu(); }
      });
    }

    /* Recherche */
    function rechercheOuverte() {
      return boutonRecherche && boutonRecherche.getAttribute("aria-expanded") === "true";
    }
    function fermerRecherche() {
      if (!boutonRecherche) return;
      boutonRecherche.setAttribute("aria-expanded", "false");
      panneauRecherche.hidden = true;
    }
    if (boutonRecherche && panneauRecherche) {
      boutonRecherche.addEventListener("click", function () {
        if (rechercheOuverte()) {
          fermerRecherche();
          return;
        }
        fermerMegas();
        if (menuOuvert()) fermerMenu();
        boutonRecherche.setAttribute("aria-expanded", "true");
        panneauRecherche.hidden = false;
        var champ = panneauRecherche.querySelector("input");
        if (champ) champ.focus();
      });
    }

    /* Touche Échap : ferme le dernier élément ouvert et rend le focus */
    document.addEventListener("keydown", function (e) {
      if (e.key !== "Escape") return;
      var mega = megaOuvert();
      if (mega && ORDINATEUR.matches) {
        fermerMegas();
        mega.focus();
      } else if (rechercheOuverte()) {
        fermerRecherche();
        boutonRecherche.focus();
      } else if (menuOuvert()) {
        fermerMenu();
        burger.focus();
      }
    });

    /* Clic en dehors de l'en-tête : ferme méga-menu et recherche */
    document.addEventListener("click", function (e) {
      if (header.contains(e.target)) return;
      if (ORDINATEUR.matches) fermerMegas();
      fermerRecherche();
    });

    /* Passage mobile <-> ordinateur : on repart d'un état propre */
    var surChangement = function () { fermerMenu(); fermerMegas(); };
    if (ORDINATEUR.addEventListener) {
      ORDINATEUR.addEventListener("change", surChangement);
    } else if (ORDINATEUR.addListener) {
      ORDINATEUR.addListener(surChangement);
    }
  }

  /* ── Démarrage ─────────────────────────────────────────────────────── */
  function init() {
    initAlertes();
    initDefilement();
    initEntete();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();


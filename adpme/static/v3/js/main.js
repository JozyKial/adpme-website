/* ==========================================================================
   ADPME Congo — main.js — v5
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

    /* ── Carrousel du bandeau d'accueil (sans défilement automatique) ──── */
  function initCarrousel() {
    document.querySelectorAll("[data-carrousel]").forEach(function (carrousel) {
      var slides = carrousel.querySelectorAll("[data-slide]");
      var points = carrousel.querySelectorAll("[data-slide-point]");
      if (slides.length < 2) return;
      var actuel = 0;

      function afficher(index) {
        actuel = (index + slides.length) % slides.length;
        slides.forEach(function (slide, i) { slide.hidden = i !== actuel; });
        points.forEach(function (point, i) {
          if (i === actuel) { point.setAttribute("aria-current", "true"); }
          else { point.removeAttribute("aria-current"); }
        });
      }

      var prec = carrousel.querySelector("[data-slide-prec]");
      var suiv = carrousel.querySelector("[data-slide-suiv]");
      if (prec) prec.addEventListener("click", function () { afficher(actuel - 1); });
      if (suiv) suiv.addEventListener("click", function () { afficher(actuel + 1); });
      points.forEach(function (point) {
        point.addEventListener("click", function () { afficher(parseInt(point.getAttribute("data-slide-point"), 10)); });
      });

      /* Glisser du doigt sur mobile */
      var departX = null;
      carrousel.addEventListener("touchstart", function (e) { departX = e.touches[0].clientX; }, { passive: true });
      carrousel.addEventListener("touchend", function (e) {
        if (departX === null) return;
        var ecart = e.changedTouches[0].clientX - departX;
        if (Math.abs(ecart) > 50) afficher(actuel + (ecart < 0 ? 1 : -1));
        departX = null;
      });
    });
  }

  /* ── FAQ : filtre instantané des questions ─────────────────────────── */
  function initFiltreFaq() {
    var champ = document.querySelector("[data-faq-filtre]");
    if (!champ) return;
    var items = Array.prototype.slice.call(document.querySelectorAll("[data-faq-item]"));
    var statut = document.querySelector("[data-faq-statut]");
    var vide = document.querySelector("[data-faq-vide]");

    function normaliser(texte) {
      return texte.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
    }
    var textes = items.map(function (item) { return normaliser(item.textContent); });

    champ.addEventListener("input", function () {
      var terme = normaliser(champ.value.trim());
      var visibles = 0;
      items.forEach(function (item, i) {
        var garde = !terme || textes[i].indexOf(terme) !== -1;
        item.hidden = !garde;
        if (garde) visibles++;
        var details = item.querySelector("details");
        if (details && terme) details.open = garde && visibles <= 3;
      });
      if (statut) statut.textContent = terme ? visibles + " question(s) trouvée(s)" : "";
      if (vide) vide.hidden = visibles > 0;
    });
  }

  /* ── Bouton « Copier le lien » ─────────────────────────────────────── */
  function initCopierLien() {
    document.querySelectorAll("[data-copier]").forEach(function (bouton) {
      bouton.addEventListener("click", function () {
        var texte = bouton.querySelector("[data-copier-texte]");
        var lien = bouton.getAttribute("data-copier");
        function confirmer(message) {
          if (!texte) return;
          var initial = texte.textContent;
          texte.textContent = message;
          window.setTimeout(function () { texte.textContent = initial; }, 2000);
        }
        if (navigator.clipboard && window.isSecureContext) {
          navigator.clipboard.writeText(lien).then(function () { confirmer("Lien copié !"); },
                                                   function () { confirmer("Copie impossible"); });
        } else {
          window.prompt("Copiez ce lien :", lien);
        }
      });
    });
  }


    /* ── Chiffres clés : compteur animé à l'apparition ─────────────────── */
  function initCompteurs() {
    var elements = document.querySelectorAll("[data-compteur]");
    if (!elements.length || !("IntersectionObserver" in window)) return;
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

    function animer(el) {
      var final = el.textContent.trim();
      /* Ex. « 1 250 », « 85 % », « +300 », « 2,5 » : on anime la partie numérique */
      var m = final.match(/^([^0-9]*)([0-9](?:[0-9\s\u00a0\u202f]*[0-9])?(?:,[0-9]+)?)(.*)$/);
      if (!m) return;
      var decimales = (m[2].split(",")[1] || "").length;
      var cible = parseFloat(m[2].replace(/[\s\u00a0\u202f]/g, "").replace(",", "."));
      if (isNaN(cible) || cible === 0) return;
      var duree = 1200, debut = null;
      function format(v) {
        return v.toLocaleString("fr-FR", { minimumFractionDigits: decimales, maximumFractionDigits: decimales });
      }
      function etape(t) {
        if (!debut) debut = t;
        var p = Math.min((t - debut) / duree, 1);
        var v = cible * (1 - Math.pow(1 - p, 3));
        el.textContent = m[1] + format(v) + m[3];
        if (p < 1) { window.requestAnimationFrame(etape); } else { el.textContent = final; }
      }
      window.requestAnimationFrame(etape);
    }

    var observateur = new IntersectionObserver(function (entrees) {
      entrees.forEach(function (entree) {
        if (entree.isIntersecting) {
          observateur.unobserve(entree.target);
          animer(entree.target);
        }
      });
    }, { threshold: 0.4 });
    elements.forEach(function (el) { observateur.observe(el); });
  }

  /* ── Démarrage ─────────────────────────────────────────────────────── */
  function init() {
    initAlertes();
    initDefilement();
    initEntete();
    initCarrousel();
    initFiltreFaq();
    initCopierLien();
    initCompteurs();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();


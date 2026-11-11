/* ==========================================================================
   ADPME Congo — main.js — v1
   JavaScript maison, sans dépendance. Chaque fonction s'active seulement si
   l'élément HTML correspondant (attribut data-…) est présent sur la page.
   ========================================================================== */
(function () {
  "use strict";

  /* ── Fermer un message (alerte Django) ─────────────────────────────── */
  function initAlertes() {
    document.querySelectorAll("[data-alerte-fermer]").forEach(function (bouton) {
      bouton.addEventListener("click", function () {
        var alerte = bouton.closest("[data-alerte]");
        if (alerte) alerte.remove();
      });
    });
  }

  /* ── Bouton « retour en haut » ─────────────────────────────────────── */
  function initRetourHaut() {
    var bouton = document.querySelector("[data-retour-haut]");
    if (!bouton) return;

    var enAttente = false;
    function maj() {
      bouton.classList.toggle("est-visible", window.scrollY > 600);
      enAttente = false;
    }
    window.addEventListener("scroll", function () {
      if (!enAttente) {
        enAttente = true;
        window.requestAnimationFrame(maj);
      }
    }, { passive: true });

    bouton.addEventListener("click", function () {
      window.scrollTo({ top: 0 });
      var contenu = document.getElementById("contenu");
      if (contenu) contenu.focus({ preventScroll: true });
    });
    maj();
  }

  /* ── Démarrage ─────────────────────────────────────────────────────── */
  function init() {
    initAlertes();
    initRetourHaut();
    /* Phase 2 : initMenu(), initMegaMenu(), initRecherche() viendront ici */
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();


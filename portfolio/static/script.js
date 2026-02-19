// Detect mobile
const isMobile = window.matchMedia("(max-width: 768px)").matches;

// Fade-in on load (desktop only)
if (!isMobile) {
  window.addEventListener("DOMContentLoaded", () => {
    document.body.classList.add("is-visible");
  });
}

// Fade-out on internal link clicks (desktop only)
document.addEventListener("click", (e) => {
  if (isMobile) return;

  const link = e.target.closest("a");
  if (!link) return;

  const url = link.getAttribute("href");
  if (!url) return;

  if (link.target === "_blank") return;
  if (link.hasAttribute("download")) return;
  if (url.startsWith("http")) return;
  if (url.startsWith("#")) return;

  e.preventDefault();

  document.body.classList.add("is-fading-out");

  setTimeout(() => {
    window.location.href = url;
  }, 185);
});
const shareBtn = document.querySelector(".share-btn");

if (shareBtn) {
  shareBtn.addEventListener("click", async () => {
    const shareData = {
      title: document.title,
      text: "Моё портфолио",
      url: window.location.href,
    };

    // Нативное меню "Поделиться" (обычно работает на телефонах)
    if (navigator.share) {
      try {
        await navigator.share(shareData);
        return;
      } catch (e) {
        // пользователь мог отменить — это нормально
      }
    }

    // Если нативного меню нет (часто на ПК) — копируем ссылку
    try {
      await navigator.clipboard.writeText(window.location.href);
      const old = shareBtn.textContent;
      shareBtn.textContent = "✓";
      setTimeout(() => (shareBtn.textContent = old), 900);
    } catch (e) {
      prompt("Скопируй ссылку:", window.location.href);
    }
  });
}


// ===== IMAGE LIGHTBOX =====
document.addEventListener("DOMContentLoaded", () => {
  const lightbox = document.getElementById("lightbox");
  const lightboxImg = document.getElementById("lightbox-img");

  document.querySelectorAll(".project-image").forEach(img => {
    img.addEventListener("click", () => {
      lightboxImg.src = img.src;
      lightbox.classList.add("active");
      document.body.style.overflow = "hidden";
    });
  });

  lightbox.addEventListener("click", () => {
    lightbox.classList.remove("active");
    lightboxImg.src = "";
    document.body.style.overflow = "";
  });

  document.addEventListener("keydown", e => {
    if (e.key === "Escape") {
      lightbox.classList.remove("active");
      lightboxImg.src = "";
      document.body.style.overflow = "";
    }
  });
});
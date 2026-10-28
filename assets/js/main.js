/* ============================================================
   Portfolio interactions — vanilla JS, no dependencies
   ============================================================ */
(function () {
  "use strict";

  const root = document.documentElement;
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Theme ---------- */
  const THEME_KEY = "nt-theme";
  const stored = localStorage.getItem(THEME_KEY);
  if (stored === "light" || stored === "dark") {
    root.setAttribute("data-theme", stored);
  } else if (window.matchMedia("(prefers-color-scheme: light)").matches) {
    root.setAttribute("data-theme", "light");
  }
  const themeMeta = document.querySelector('meta[name="theme-color"]');
  const syncMeta = () =>
    themeMeta && themeMeta.setAttribute("content", root.getAttribute("data-theme") === "light" ? "#f6f7fc" : "#0b1020");
  syncMeta();

  const themeToggle = document.getElementById("themeToggle");
  themeToggle?.addEventListener("click", () => {
    const next = root.getAttribute("data-theme") === "light" ? "dark" : "light";
    root.setAttribute("data-theme", next);
    localStorage.setItem(THEME_KEY, next);
    syncMeta();
  });

  /* ---------- Mobile menu ---------- */
  const nav = document.getElementById("nav");
  const menuBtn = document.getElementById("menuBtn");
  const closeMenu = () => {
    nav?.classList.remove("open");
    menuBtn?.setAttribute("aria-expanded", "false");
  };
  menuBtn?.addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    menuBtn.setAttribute("aria-expanded", String(open));
  });
  nav?.addEventListener("click", (e) => {
    if (e.target.tagName === "A") closeMenu();
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeMenu();
  });

  /* ---------- Header state + progress + back to top ---------- */
  const header = document.getElementById("siteHeader");
  const progress = document.getElementById("scrollProgress");
  const toTop = document.getElementById("toTop");

  const onScroll = () => {
    const y = window.scrollY || 0;
    header?.classList.toggle("scrolled", y > 8);
    const max = document.documentElement.scrollHeight - window.innerHeight;
    if (progress) progress.style.width = max > 0 ? (y / max) * 100 + "%" : "0%";
    toTop?.classList.toggle("show", y > 560);
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- Active nav link ---------- */
  const sections = Array.from(document.querySelectorAll("main section[id]"));
  const navLinks = Array.from(document.querySelectorAll('.nav a[href^="#"]'));
  if ("IntersectionObserver" in window && sections.length) {
    const spy = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          const id = entry.target.id;
          navLinks.forEach((a) => a.classList.toggle("active", a.getAttribute("href") === "#" + id));
        });
      },
      { rootMargin: "-45% 0px -50% 0px", threshold: 0 }
    );
    sections.forEach((s) => spy.observe(s));
  }

  /* ---------- Reveal on scroll ---------- */
  const revealEls = document.querySelectorAll(".reveal");
  if (reduceMotion || !("IntersectionObserver" in window)) {
    revealEls.forEach((el) => el.classList.add("in"));
  } else {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("in");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );
    revealEls.forEach((el) => io.observe(el));
  }

  /* ---------- Skill bars ---------- */
  const bars = document.querySelectorAll(".bar-track i");
  const fillBars = (scope) => scope.forEach((b) => b.classList.add("filled"));
  if (reduceMotion || !("IntersectionObserver" in window)) {
    fillBars(bars);
  } else {
    const barIo = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("filled");
            barIo.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.4 }
    );
    bars.forEach((b) => barIo.observe(b));
  }

  /* ---------- Typing effect for hero role ---------- */
  const typed = document.getElementById("typed");
  const phrases = [
    ".NET Software Engineer",
    "Angular & ASP.NET Core Developer",
    "ERP Systems Specialist",
    "Full-Stack .NET Developer",
  ];
  if (typed) {
    if (reduceMotion) {
      typed.textContent = phrases[0];
    } else {
      let p = 0, i = phrases[0].length, deleting = false;
      const tick = () => {
        const word = phrases[p];
        if (!deleting) {
          i++;
          typed.textContent = word.slice(0, i);
          if (i >= word.length) {
            deleting = true;
            return setTimeout(tick, 1900);
          }
          return setTimeout(tick, 55);
        }
        i--;
        typed.textContent = word.slice(0, i);
        if (i <= 0) {
          deleting = false;
          p = (p + 1) % phrases.length;
          return setTimeout(tick, 320);
        }
        setTimeout(tick, 26);
      };
      setTimeout(() => {
        deleting = true;
        tick();
      }, 2200);
    }
  }

  /* ---------- Contact form → mailto ---------- */
  const form = document.getElementById("contactForm");
  const status = document.getElementById("formStatus");
  form?.addEventListener("submit", (e) => {
    e.preventDefault();
    const data = new FormData(form);
    const name = String(data.get("name") || "").trim();
    const email = String(data.get("email") || "").trim();
    const subject = String(data.get("subject") || "").trim() || "Portfolio enquiry";
    const message = String(data.get("message") || "").trim();

    if (!name || !email || !message) {
      if (status) {
        status.textContent = "Please fill in your name, email and message.";
        status.classList.add("err");
      }
      return;
    }

    const body = `Name: ${name}\nEmail: ${email}\n\n${message}`;
    const href =
      "mailto:nizamddin2001@gmail.com?subject=" +
      encodeURIComponent(subject + " — " + name) +
      "&body=" +
      encodeURIComponent(body);

    window.location.href = href;
    if (status) {
      status.classList.remove("err");
      status.textContent = "Opening your email app… if nothing happens, email nizamddin2001@gmail.com directly.";
    }
  });

  /* ---------- Year ---------- */
  const yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());
})();

/* ── Element refs ─────────────────────────────────────────────────── */
const routeSelect     = document.getElementById("routeSelect");
const directionSelect = document.getElementById("directionSelect");
const searchBtn       = document.getElementById("searchBtn");
const resultsSection  = document.getElementById("resultsSection");
const resultsTitle    = document.getElementById("resultsTitle");
const resultsCount    = document.getElementById("resultsCount");
const timetableBody   = document.getElementById("timetableBody");
const loadingState    = document.getElementById("loadingState");
const emptyState      = document.getElementById("emptyState");

/* ── Helpers ──────────────────────────────────────────────────────── */
function setVisible(el, visible) {
  el.hidden = !visible;
}

function resetDirections() {
  directionSelect.innerHTML = '<option value="">— Select a direction —</option>';
  directionSelect.disabled = true;
  searchBtn.disabled = true;
  setVisible(resultsSection, false);
  setVisible(emptyState, false);
}

/* ── Route dropdown change ───────────────────────────────────────── */
routeSelect.addEventListener("change", async () => {
  resetDirections();

  const routeId = routeSelect.value;
  if (!routeId) return;

  try {
    const res  = await fetch(`/api/directions?route_id=${encodeURIComponent(routeId)}`);
    const dirs = await res.json();

    dirs.forEach(dir => {
      const opt = document.createElement("option");
      opt.value       = dir;
      opt.textContent = dir;
      directionSelect.appendChild(opt);
    });

    directionSelect.disabled = false;
  } catch (err) {
    console.error("Failed to load directions:", err);
  }
});

/* ── Direction dropdown change ───────────────────────────────────── */
directionSelect.addEventListener("change", () => {
  searchBtn.disabled = !directionSelect.value;
  setVisible(resultsSection, false);
  setVisible(emptyState, false);
});

/* ── Search button click ─────────────────────────────────────────── */
searchBtn.addEventListener("click", async () => {
  const routeId   = routeSelect.value;
  const direction = directionSelect.value;
  if (!routeId || !direction) return;

  // Show loading
  setVisible(resultsSection, false);
  setVisible(emptyState, false);
  setVisible(loadingState, true);

  try {
    const url = `/api/timetable?route_id=${encodeURIComponent(routeId)}&direction=${encodeURIComponent(direction)}`;
    const res  = await fetch(url);
    const rows = await res.json();

    setVisible(loadingState, false);

    if (!rows.length) {
      setVisible(emptyState, true);
      return;
    }

    // Build title from selected option labels
    const routeLabel = routeSelect.options[routeSelect.selectedIndex].text;
    const cardinals = ["East", "West", "North", "South"];
    const dirLabel = cardinals.includes(direction) ? `${direction}bound` : direction;
    resultsTitle.textContent = `${routeLabel}  ·  ${dirLabel}`;
    resultsCount.textContent = `${rows.length} stop${rows.length !== 1 ? "s" : ""}`;

    // Populate table
    timetableBody.innerHTML = "";
    rows.forEach((row, idx) => {
      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td>${idx + 1}</td>
        <td>${row.arrival_time ?? "—"}</td>
        <td>${row.departure_time ?? "—"}</td>
        <td>${row.stop_name ?? "—"}</td>
      `;
      timetableBody.appendChild(tr);
    });

    setVisible(resultsSection, true);

    // Scroll results into view smoothly
    resultsSection.scrollIntoView({ behavior: "smooth", block: "start" });

  } catch (err) {
    console.error("Failed to load timetable:", err);
    setVisible(loadingState, false);
    setVisible(emptyState, true);
  }
});

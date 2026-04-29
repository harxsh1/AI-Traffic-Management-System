let running = false;

function setLights(greenLane) {
  // reset all
  ["red1","yellow1","green1","red2","yellow2","green2"]
    .forEach(id => document.getElementById(id).classList.remove("active"));

  if (greenLane === 1) {
    document.getElementById("green1").classList.add("active");
    document.getElementById("red2").classList.add("active");
  } else {
    document.getElementById("green2").classList.add("active");
    document.getElementById("red1").classList.add("active");
  }
}

async function fetchData() {
  const res = await fetch("http://127.0.0.1:5000/data");
  const data = await res.json();

  document.getElementById("density").innerText =
    "Lane Counts: " + data.lane_counts.join(", ");

  document.getElementById("decision").innerText =
    "Green Lane: " + data.green_lane;

  return data;
}

async function runSystem() {
  if (!running) return;

  document.getElementById("status").innerText = "Running...";

  const data = await fetchData();

  setLights(data.green_lane);

  setTimeout(runSystem, data.green_time * 1000);
}

function startSystem() {
  running = true;
  runSystem();
}

function stopSystem() {
  running = false;
  document.getElementById("status").innerText = "Stopped";
}
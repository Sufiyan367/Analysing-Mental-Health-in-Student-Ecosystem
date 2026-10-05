/**
 * static/js/main.js
 * Client-side script handling Tableau visual sizing and responsiveness.
 */

document.addEventListener('DOMContentLoaded', () => {
  console.log("Mental Health in Student Ecosystem Visualizer Initialized.");

  // Check if there is an active tableau placeholder
  const placeholder = document.querySelector('.tableauPlaceholder');
  if (placeholder) {
    const adjustHeight = () => {
      const containerWidth = placeholder.offsetWidth;
      // Adjust aspect ratio if on desktop vs mobile
      if (containerWidth > 900) {
        placeholder.style.minHeight = "800px";
      } else {
        placeholder.style.minHeight = "600px";
      }
    };
    adjustHeight();
    window.addEventListener('resize', adjustHeight);
  }
});

/* -- Glow effect -- */

const blob = document.getElementById("blob");
const blob2 = document.getElementById("blob2");

window.onpointermove = event => {
    const { clientX, clientY } = event;

    blob.animate({
        left: `${clientX}px`,
        top: `${clientY}px`
    }, { duration: 3000, fill: "forwards" });
}
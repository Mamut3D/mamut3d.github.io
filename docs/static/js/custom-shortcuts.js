// https://www.w3schools.com/howto/howto_js_fullscreen.asp
/* Get the documentElement (<html>) to display the page in fullscreen */
var elem = document.documentElement;

/* View in fullscreen */
function openFullscreen() {
  if (elem.requestFullscreen) {
    elem.requestFullscreen();
  } else if (elem.webkitRequestFullscreen) { /* Safari */
    elem.webkitRequestFullscreen();
  } else if (elem.msRequestFullscreen) { /* IE11 */
    elem.msRequestFullscreen();
  }
}

/* Close fullscreen */
function closeFullscreen() {
  if (document.exitFullscreen) {
    document.exitFullscreen();
  } else if (document.webkitExitFullscreen) { /* Safari */
    document.webkitExitFullscreen();
  } else if (document.msExitFullscreen) { /* IE11 */
    document.msExitFullscreen();
  }
}

// Keyboad shortcuts
// So far quick and dirty, but it will be improved ;-)
document.addEventListener('keyup', (e) => {
  if (document.activeElement != document.getElementById("search-by")) {
    // show keyboard shortcut info on 'i' keypress
    if (e.key.toLowerCase() === 'i') {
      alert(
"Keyboard shortcuts: \n\n \
i  -  this keyboard shortcut info \n \
/  -  focus search bar \n \
f  -  fullscrean (F11 on Android don't work) \n \
h  -  navigate on previous page \n \
l  -  navigate on next page \n \
j  -  scroll down \n \
alt + j  -  scroll down big\n \
k  -  scroll up \n \
alt + k  -  scroll up big \n \
g  -  scroll to the top \n \
G  -  scroll to the end"
      );
    }
    // focus search on '/' key
    if (e.key.toLowerCase() === '/') {
      //alert('/ key pressed');
      // show naviagation bar (important on mobile)
      var b = document.querySelector( 'body' );
      // run show menu toggle only when hidden
      if( !b.classList.contains( 'sidebar-flyout' ) ) {
        showNav();
      }
      document.getElementById("search-by").focus();
    }
    // vim style keys
    // navigate to following page on 'l' key
    if (e.key.toLowerCase() === 'l') {
      jQuery('a.nav-next').click();
    }
    // navigate to previous page on 'h' key
    if (e.key.toLowerCase() === 'h') {
      jQuery('a.nav-prev').click();
    }

    // navigate to previous page on 'h' key
    if (e.key.toLowerCase() === 'f') {
      if (window.innerHeight == screen.height) {
        closeFullscreen();
      } else {
        openFullscreen();
      }
    }

    // scroll up and down via 'j' and 'k' was hacked in
    // static/js/perfect-scrollbar.min.js
    // static/js/theme.js
  }
});

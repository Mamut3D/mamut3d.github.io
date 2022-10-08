---
layout: post
title:  "Hope Harder keyboard shortcuts"
date:   2022-10-08 12:00:00 +0100
weight: 4
---

<!-- vim-markdown-toc GFM -->

* [The obsession](#the-obsession)
* [Keyboard shortcuts to Hugo relearn theme](#keyboard-shortcuts-to-hugo-relearn-theme)
	* [Switch between articles](#switch-between-articles)
	* [Scroll articles](#scroll-articles)
	* [Focus search input](#focus-search-input)
	* [Key shortcut info](#key-shortcut-info)
* [Conclusion](#conclusion)

<!-- vim-markdown-toc -->

## The obsession

As a long time computer user - basically for the whole 21st century and a bit before that - I have grown into an age, where I am bored by all the fancy new GUIs, clickable whatevers, shiny new Apple ding dongs and am obsessed with the ability to control the computer only with the keyboard and digesting only the information I need.

To achieve this, I spend my time in the place where I feel most at home - the terminal with its command line applications, "graphical"/ncurses apps and many keyboard shortcuts which allow fast paced use of the machine, without the need to touch the screen or mouse.

There is a method to madness as they say, and after a while I found out, that many keyboard shortcuts can be observed in different places. Mainly the patterns such as:
- `CTRL + NUM` - tends to switch between panels such as tabs in browsers, sessions in Termux, sessions in Windows Terminal...
- `WIN + NUM` - tends to switch between or start applications based on their order in Taskbar in Windows, Dex...
- `WIN` - tends to open some search bar for apps in OS linux desktops, Windows, Dex...
- `/` - focuses on the search bar on many websites such as Google, GitLab, GitHub...
- `hjkl` - is used as arrow keys in Vim in normal mode

Some time ago I started practicing typing with all ten fingers and acquired some typist skill. Not much yet, since I am currently at approximately 60wpm on my good day, but it's something I guess.

![It's something](/blog/2022-10-08-hope-harder-keyboard-shortcuts/its-something.jpg)

What feels great to me about typing in Vim is the use of `hjkl` as arrow keys in normal mode. It is awesome, because the keys are right under your finger resting position and thus can be used almost without movement of a finger :-). I have dearly missed the last two keyboard shortcuts mentioned in the list and their absence made the use of my personal KB a chore. So it tried to implement these shortcuts within this shiny web page.

## Keyboard shortcuts to Hugo relearn theme

Relearn as a whole already has some shortcuts implemented. But I actually only found them as an accident when looking through the code of the theme. Through trial and error, I have found that in Relearn there are implemented these shortcuts:

- `left`/`right` - to switch between articles
- `up`/`down` - to scroll articles
- `CTRL` + `m` - show side menu (useful on small screens)

I have also found that you can add your custom scripts to Relearn by adding js in `<script>` tag to `layouts/partials/custom-footer.html`.

### Switch between articles

I discovered the implementation for article switching in `themes/relearn/static/js/theme.js`:

```js
// keyboard navigation
jQuery(document).keydown(function(e) {
  if(e.which == '37') {
    jQuery('a.nav-prev').click();
  }
  if(e.which == '39') {
    jQuery('a.nav-next').click();
  }
});
```

It was pretty easy to locate keyCodes for `h` and `l` and copy the code to `custom-footer` and it worked like a charm. Now I can switch between articles in Vim style.

### Scroll articles

This one sucked. I learned that for scrolling Relearn uses [PerfectScrollbar](https://perfectscrollbar.com) as a js library in `themes/relearn/static/js/perfect-scrollbar.min.js`. The code was compacted to save bandwidth and as is is pretty unreadable. I used [js-beautify](https://www.google.com/search?q=npm+js-beautify&oq=npm+js-beau&aqs=chrome.2.69i57j69i60j0i512j0i22i30l2j0i390.9354j0j7&sourceid=chrome-mobile&ie=UTF-8) utility and searched for the code responsible for handling of `up` and `down` scrolling in a long case statement.

Long story short, I was not able to add `j` and `k` shortcut using `custom-footer`. I overridded the library and added another `case` to handle `j` and `k`key press events. It's ugly, but it works.
```js
// static/js/perfect-scrollbar.min.js
a.event.bind(a.ownerDocument, "keydown", function(d) {
    if (!(d.isDefaultPrevented && d.isDefaultPrevented() || d.defaultPrevented) && (f() || g())) {
        var e = document.activeElement ? document.activeElement : a.ownerDocument.activeElement;
        if (e) {
            if ("IFRAME" === e.tagName) e = e.contentDocument.activeElement;
            else // go deeper if element is a webcomponent
                for (; e.shadowRoot;) e = e.shadowRoot.activeElement;
            if (o(e)) return
        }
        var h = 0,
            i = 0;
        switch (d.which) {
            case 37:
                h = d.metaKey ? -a.contentWidth : d.altKey ? -a.containerWidth : -30;
                break;
	    // original arrow up handler
            case 38:
                i = d.metaKey ? a.contentHeight : d.altKey ? a.containerHeight : 30;
                break;
	    // injected case 'k'
            case 75:
                i = d.metaKey ? a.contentHeight : d.altKey ? a.containerHeight : 30;
                break;
            case 39:
                h = d.metaKey ? a.contentWidth : d.altKey ? a.containerWidth : 30;
                break;
	    // original arrow down handler
            case 40:
                i = d.metaKey ? -a.contentHeight : d.altKey ? -a.containerHeight : -30;
                break;
	    // injected case 'j'
            case 74:
                i = d.metaKey ? -a.contentHeight : d.altKey ? -a.containerHeight : -30;
                break;
            case 32:
                i = d.shiftKey ? a.containerHeight : -a.containerHeight;
                break;
            case 33:
                i = a.containerHeight;
                break;
            case 34:
                i = -a.containerHeight;
                break;
            case 36:
                i = a.contentHeight;
                break;
            case 35:
                i = -a.contentHeight;
                break;
            default:
                return;
        }
        a.settings.suppressScrollX && 0 !== h || a.settings.suppressScrollY && 0 !== i || (c.scrollTop -= i, c.scrollLeft += h, q(a), b(h, i) && d.preventDefault())
    }
})
```

### Focus search input

Oh, this feature I missed the most. The ability to move to search bar with just a '/' key press. I have googled a bit and solution immediately popped out:

```js
document.addEventListener('keyup', (e) => {
  // focus search on '/' key
  if (e.key.toLowerCase() === '/') {
    document.getElementById("search-by").focus();
  }
}
```

It worked great. Actually this was the first shortcut I added. But after I added another shortcuts, few bugs occured:

- Once '/' pressed (and relieved keyUp) focus moved to search input field. However when I pressed other shortcuts like 'l' for next article, instead of adding letter 'l' to search field, I was taken to next article. Solution? Disable shortcuts when search input field is focused.

  ```js
  // Check if search input is focused and disable other shortcuts if true
  document.addEventListener('keyup', (e) => {
    if (document.activeElement != document.getElementById("search-by")) {
      // focus search on '/' key
      if (e.key.toLowerCase() === '/') {
        document.getElementById("search-by").focus();
      }
      // ...
      // other shortcuts
    }
  }
  ```
- When `/` key is pressed on small screen Android mobile phone, sidebar with search is hidden. Search field is focused but not displayed. I browsed through the code and found a function that toggles navigation sidebar visibility in Relearn theme 'showNav()' and extended `/` key press logic with it.

  ```js
  // Check if search input is focused and disable other shortcuts if true
  document.addEventListener('keyup', (e) => {
    if (document.activeElement != document.getElementById("search-by")) {
      // focus search on '/' key
      if (e.key.toLowerCase() === '/') {
        document.getElementById("search-by").focus();
        // show naviagation bar (important on mobile)
        var b = document.querySelector( 'body' );
        // run show menu toggle only when hidden
        if( !b.classList.contains( 'sidebar-flyout' ) ) {
	  // show navigation bar toggle function from Relearn theme
          showNav();
        }
      }
      // ...
      // other shortcuts
    }
  }
  ```

### Key shortcut info

Help is always appreciated so I added JavaScript `alert()` function to show help on `i` key press. I learned that JavaScript does not have any way, without additional library, how to wrap multi line string and keep pretty indentation:

```js
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
alt + k  -  scroll up big"
 );
}
```

## Conclusion

Awesome keyboard shortcuts can be easily added to Hugo Relearn theme based web pages. I scratched the JavaScript surface a bit without previous experience and I think that I start to see, why some people think it pretty much sucks :-). I am quite happy with the end result and now I can use my KB without the need to touch mouse. I feels so good!

![Feels](/blog/2022-10-08-hope-harder-keyboard-shortcuts/so-good.png)

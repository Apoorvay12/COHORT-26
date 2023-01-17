<!DOCTYPE html>
<!-- saved from url=(0110)https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion -->
<html dir="ltr" lang="en-US"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
   <!-- Global site tag (gtag.js) - Google Analytics -->
   <script src="./a8_q8_files/twk-main.js.download" charset="UTF-8" crossorigin="*"></script><script src="./a8_q8_files/twk-vendor.js.download" charset="UTF-8" crossorigin="*"></script><script src="./a8_q8_files/twk-chunk-vendors.js.download" charset="UTF-8" crossorigin="*"></script><script src="./a8_q8_files/twk-chunk-common.js.download" charset="UTF-8" crossorigin="*"></script><script src="./a8_q8_files/twk-runtime.js.download" charset="UTF-8" crossorigin="*"></script><script src="./a8_q8_files/twk-app.js.download" charset="UTF-8" crossorigin="*"></script><script src="./a8_q8_files/cb=gapi.loaded_2" async=""></script><script src="./a8_q8_files/cb=gapi.loaded_1" async=""></script><script src="./a8_q8_files/cb=gapi.loaded_0" async=""></script><script type="text/javascript" async="" src="./a8_q8_files/atrk.js.download"></script><script async="" src="./a8_q8_files/default" charset="UTF-8" crossorigin="*"></script><script type="text/javascript" async="" src="./a8_q8_files/analytics.js.download"></script><script type="text/javascript" async="" src="./a8_q8_files/js"></script><script async="" src="./a8_q8_files/js(1)"></script>
   <script>
      window.dataLayer = window.dataLayer || [];
      function gtag() { dataLayer.push(arguments); }
      gtag('js', new Date());

      gtag('config', 'UA-109728305-1');
   </script>
   <meta name="google-site-verification" content="p2kNyH1NDKhkZLl2aBdmmvosWqHZOxD0rmvS1n8LcDA">
   <meta name="google-signin-client_id" content="458958442206-nstdi8m8r1ru8qbfd9qmpmhllq5gbui7.apps.googleusercontent.com">
         
         
         
   <title>PepCoding | Rotate A Number</title>
   <link rel="shortcut icon" href="https://www.pepcoding.com/images/favicon.ico">
   <link rel="apple-touch-icon-precomposed" href="https://www.pepcoding.com/images/apple-touch-icon.png">
   <meta property="og:url" content="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion">
   <meta property="title" content="PepCoding | Rotate A Number">
   <meta property="og:title" content="PepCoding | Rotate A Number">
   <meta property="keywords" content="">
   <meta property="og:image" content="https://www.pepcoding.com/images/logo.png">
   <meta property="og:alt" content="pepcoding">
   <meta property="og:type" content="website">
   <meta name="description" content="java basics, basic programming, learn java, pepcoding, pepcoding online, sumeet malik, learn java for free, free java">
   <meta property="og:description" content="java basics, basic programming, learn java, pepcoding, pepcoding online, sumeet malik, learn java for free, free java">
   <script type="application/ld+json">
         {
           "@context" : "http://schema.org",
           "@type": "EducationalOrganization",
           "name" : "Pepcoding",
           "url" : "https://www.pepcoding.com",
           "logo":"https://www.pepcoding.com/images/logo.png",
           "description": "Free online videos of Data Structure using Java and C++. Best coding institute in Delhi, Best computer programming institute in Delhi, Best java training classes, Coding classes in Delhi, Coding courses in Delhi, best computer programming institute in Delhi-NCR, Delhi's best programming institute offers courses in Java, C++, Web Development, Nodejs.",
          "sameAs" : [
            "https://www.facebook.com/pepcoding/",
            "https://www.youtube.com/results?search_query=pepcoding",
            "https://www.instagram.com/pepcoding/",
            "https://in.linkedin.com/company/pepcoding-education",
            "https://twitter.com/pepcoding"
            ],
         
          "openingHours": "Mo 08:30-21:30 Tu, We 08:00-21:30 Th, Fr, Sa, Su 08:00-09:30",
           "contactPoint": {
             "@type": "ContactPoint",
             "telephone": "011-40194461",
             "contactType": "Reception desk"
           },
          "address": {
             "@type": "PostalAddress",
             "streetAddress": "PepCoding, 3rd Floor, 15 Vaishali, Pitampura Opposite",
             "addressLocality": "Pitampura",
             "addressRegion": "Delhi",
             "postalCode": "110034",
             "addressCountry": "India"
           },
            "hasMap": "https://www.google.com/maps/place/PepCoding.com/@28.699367,77.138281,17z/data=!4m5!3m4!1s0x0:0x4fd0fdfc3f27ffaf!8m2!3d28.6993666!4d77.1382814?hl=en-US"
         }
      </script>
   <link rel="stylesheet" href="./a8_q8_files/site.css">
   <link rel="stylesheet" href="./a8_q8_files/video.css">
   
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <link href="./a8_q8_files/css" rel="stylesheet">
   <link href="./a8_q8_files/font-awesome.min.css" rel="stylesheet">
<style id="ace_editor.css">.ace_editor {position: relative;overflow: hidden;font: 12px/normal 'Monaco', 'Menlo', 'Ubuntu Mono', 'Consolas', 'source-code-pro', monospace;direction: ltr;text-align: left;}.ace_scroller {position: absolute;overflow: hidden;top: 0;bottom: 0;background-color: inherit;-ms-user-select: none;-moz-user-select: none;-webkit-user-select: none;user-select: none;cursor: text;}.ace_content {position: absolute;-moz-box-sizing: border-box;-webkit-box-sizing: border-box;box-sizing: border-box;min-width: 100%;}.ace_dragging .ace_scroller:before{position: absolute;top: 0;left: 0;right: 0;bottom: 0;content: '';background: rgba(250, 250, 250, 0.01);z-index: 1000;}.ace_dragging.ace_dark .ace_scroller:before{background: rgba(0, 0, 0, 0.01);}.ace_selecting, .ace_selecting * {cursor: text !important;}.ace_gutter {position: absolute;overflow : hidden;width: auto;top: 0;bottom: 0;left: 0;cursor: default;z-index: 4;-ms-user-select: none;-moz-user-select: none;-webkit-user-select: none;user-select: none;}.ace_gutter-active-line {position: absolute;left: 0;right: 0;}.ace_scroller.ace_scroll-left {box-shadow: 17px 0 16px -16px rgba(0, 0, 0, 0.4) inset;}.ace_gutter-cell {padding-left: 19px;padding-right: 6px;background-repeat: no-repeat;}.ace_gutter-cell.ace_error {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAABOFBMVEX/////////QRswFAb/Ui4wFAYwFAYwFAaWGAfDRymzOSH/PxswFAb/SiUwFAYwFAbUPRvjQiDllog5HhHdRybsTi3/Tyv9Tir+Syj/UC3////XurebMBIwFAb/RSHbPx/gUzfdwL3kzMivKBAwFAbbvbnhPx66NhowFAYwFAaZJg8wFAaxKBDZurf/RB6mMxb/SCMwFAYwFAbxQB3+RB4wFAb/Qhy4Oh+4QifbNRcwFAYwFAYwFAb/QRzdNhgwFAYwFAbav7v/Uy7oaE68MBK5LxLewr/r2NXewLswFAaxJw4wFAbkPRy2PyYwFAaxKhLm1tMwFAazPiQwFAaUGAb/QBrfOx3bvrv/VC/maE4wFAbRPBq6MRO8Qynew8Dp2tjfwb0wFAbx6eju5+by6uns4uH9/f36+vr/GkHjAAAAYnRSTlMAGt+64rnWu/bo8eAA4InH3+DwoN7j4eLi4xP99Nfg4+b+/u9B/eDs1MD1mO7+4PHg2MXa347g7vDizMLN4eG+Pv7i5evs/v79yu7S3/DV7/498Yv24eH+4ufQ3Ozu/v7+y13sRqwAAADLSURBVHjaZc/XDsFgGIBhtDrshlitmk2IrbHFqL2pvXf/+78DPokj7+Fz9qpU/9UXJIlhmPaTaQ6QPaz0mm+5gwkgovcV6GZzd5JtCQwgsxoHOvJO15kleRLAnMgHFIESUEPmawB9ngmelTtipwwfASilxOLyiV5UVUyVAfbG0cCPHig+GBkzAENHS0AstVF6bacZIOzgLmxsHbt2OecNgJC83JERmePUYq8ARGkJx6XtFsdddBQgZE2nPR6CICZhawjA4Fb/chv+399kfR+MMMDGOQAAAABJRU5ErkJggg==");background-repeat: no-repeat;background-position: 2px center;}.ace_gutter-cell.ace_warning {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAmVBMVEX///8AAAD///8AAAAAAABPSzb/5sAAAAB/blH/73z/ulkAAAAAAAD85pkAAAAAAAACAgP/vGz/rkDerGbGrV7/pkQICAf////e0IsAAAD/oED/qTvhrnUAAAD/yHD/njcAAADuv2r/nz//oTj/p064oGf/zHAAAAA9Nir/tFIAAAD/tlTiuWf/tkIAAACynXEAAAAAAAAtIRW7zBpBAAAAM3RSTlMAABR1m7RXO8Ln31Z36zT+neXe5OzooRDfn+TZ4p3h2hTf4t3k3ucyrN1K5+Xaks52Sfs9CXgrAAAAjklEQVR42o3PbQ+CIBQFYEwboPhSYgoYunIqqLn6/z8uYdH8Vmdnu9vz4WwXgN/xTPRD2+sgOcZjsge/whXZgUaYYvT8QnuJaUrjrHUQreGczuEafQCO/SJTufTbroWsPgsllVhq3wJEk2jUSzX3CUEDJC84707djRc5MTAQxoLgupWRwW6UB5fS++NV8AbOZgnsC7BpEAAAAABJRU5ErkJggg==");background-position: 2px center;}.ace_gutter-cell.ace_info {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAAAAAA6mKC9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAJ0Uk5TAAB2k804AAAAPklEQVQY02NgIB68QuO3tiLznjAwpKTgNyDbMegwisCHZUETUZV0ZqOquBpXj2rtnpSJT1AEnnRmL2OgGgAAIKkRQap2htgAAAAASUVORK5CYII=");background-position: 2px center;}.ace_dark .ace_gutter-cell.ace_info {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAAJFBMVEUAAAChoaGAgIAqKiq+vr6tra1ZWVmUlJSbm5s8PDxubm56enrdgzg3AAAAAXRSTlMAQObYZgAAAClJREFUeNpjYMAPdsMYHegyJZFQBlsUlMFVCWUYKkAZMxZAGdxlDMQBAG+TBP4B6RyJAAAAAElFTkSuQmCC");}.ace_scrollbar {position: absolute;right: 0;bottom: 0;z-index: 6;}.ace_scrollbar-inner {position: absolute;cursor: text;left: 0;top: 0;}.ace_scrollbar-v{overflow-x: hidden;overflow-y: scroll;top: 0;}.ace_scrollbar-h {overflow-x: scroll;overflow-y: hidden;left: 0;}.ace_print-margin {position: absolute;height: 100%;}.ace_text-input {position: absolute;z-index: 0;width: 0.5em;height: 1em;opacity: 0;background: transparent;-moz-appearance: none;appearance: none;border: none;resize: none;outline: none;overflow: hidden;font: inherit;padding: 0 1px;margin: 0 -1px;text-indent: -1em;-ms-user-select: text;-moz-user-select: text;-webkit-user-select: text;user-select: text;white-space: pre!important;}.ace_text-input.ace_composition {background: inherit;color: inherit;z-index: 1000;opacity: 1;text-indent: 0;}.ace_layer {z-index: 1;position: absolute;overflow: hidden;word-wrap: normal;white-space: pre;height: 100%;width: 100%;-moz-box-sizing: border-box;-webkit-box-sizing: border-box;box-sizing: border-box;pointer-events: none;}.ace_gutter-layer {position: relative;width: auto;text-align: right;pointer-events: auto;}.ace_text-layer {font: inherit !important;}.ace_cjk {display: inline-block;text-align: center;}.ace_cursor-layer {z-index: 4;}.ace_cursor {z-index: 4;position: absolute;-moz-box-sizing: border-box;-webkit-box-sizing: border-box;box-sizing: border-box;border-left: 2px solid;transform: translatez(0);}.ace_slim-cursors .ace_cursor {border-left-width: 1px;}.ace_overwrite-cursors .ace_cursor {border-left-width: 0;border-bottom: 1px solid;}.ace_hidden-cursors .ace_cursor {opacity: 0.2;}.ace_smooth-blinking .ace_cursor {-webkit-transition: opacity 0.18s;transition: opacity 0.18s;}.ace_editor.ace_multiselect .ace_cursor {border-left-width: 1px;}.ace_marker-layer .ace_step, .ace_marker-layer .ace_stack {position: absolute;z-index: 3;}.ace_marker-layer .ace_selection {position: absolute;z-index: 5;}.ace_marker-layer .ace_bracket {position: absolute;z-index: 6;}.ace_marker-layer .ace_active-line {position: absolute;z-index: 2;}.ace_marker-layer .ace_selected-word {position: absolute;z-index: 4;-moz-box-sizing: border-box;-webkit-box-sizing: border-box;box-sizing: border-box;}.ace_line .ace_fold {-moz-box-sizing: border-box;-webkit-box-sizing: border-box;box-sizing: border-box;display: inline-block;height: 11px;margin-top: -2px;vertical-align: middle;background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="),url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACJJREFUeNpi+P//fxgTAwPDBxDxD078RSX+YeEyDFMCIMAAI3INmXiwf2YAAAAASUVORK5CYII=");background-repeat: no-repeat, repeat-x;background-position: center center, top left;color: transparent;border: 1px solid black;border-radius: 2px;cursor: pointer;pointer-events: auto;}.ace_dark .ace_fold {}.ace_fold:hover{background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="),url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACBJREFUeNpi+P//fz4TAwPDZxDxD5X4i5fLMEwJgAADAEPVDbjNw87ZAAAAAElFTkSuQmCC");}.ace_tooltip {background-color: #FFF;background-image: -webkit-linear-gradient(top, transparent, rgba(0, 0, 0, 0.1));background-image: linear-gradient(to bottom, transparent, rgba(0, 0, 0, 0.1));border: 1px solid gray;border-radius: 1px;box-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);color: black;max-width: 100%;padding: 3px 4px;position: fixed;z-index: 999999;-moz-box-sizing: border-box;-webkit-box-sizing: border-box;box-sizing: border-box;cursor: default;white-space: pre;word-wrap: break-word;line-height: normal;font-style: normal;font-weight: normal;letter-spacing: normal;pointer-events: none;}.ace_folding-enabled > .ace_gutter-cell {padding-right: 13px;}.ace_fold-widget {-moz-box-sizing: border-box;-webkit-box-sizing: border-box;box-sizing: border-box;margin: 0 -12px 0 1px;display: none;width: 11px;vertical-align: top;background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42mWKsQ0AMAzC8ixLlrzQjzmBiEjp0A6WwBCSPgKAXoLkqSot7nN3yMwR7pZ32NzpKkVoDBUxKAAAAABJRU5ErkJggg==");background-repeat: no-repeat;background-position: center;border-radius: 3px;border: 1px solid transparent;cursor: pointer;}.ace_folding-enabled .ace_fold-widget {display: inline-block;   }.ace_fold-widget.ace_end {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42m3HwQkAMAhD0YzsRchFKI7sAikeWkrxwScEB0nh5e7KTPWimZki4tYfVbX+MNl4pyZXejUO1QAAAABJRU5ErkJggg==");}.ace_fold-widget.ace_closed {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAGCAYAAAAG5SQMAAAAOUlEQVR42jXKwQkAMAgDwKwqKD4EwQ26sSOkVWjgIIHAzPiCgaqiqnJHZnKICBERHN194O5b9vbLuAVRL+l0YWnZAAAAAElFTkSuQmCCXA==");}.ace_fold-widget:hover {border: 1px solid rgba(0, 0, 0, 0.3);background-color: rgba(255, 255, 255, 0.2);box-shadow: 0 1px 1px rgba(255, 255, 255, 0.7);}.ace_fold-widget:active {border: 1px solid rgba(0, 0, 0, 0.4);background-color: rgba(0, 0, 0, 0.05);box-shadow: 0 1px 1px rgba(255, 255, 255, 0.8);}.ace_dark .ace_fold-widget {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHklEQVQIW2P4//8/AzoGEQ7oGCaLLAhWiSwB146BAQCSTPYocqT0AAAAAElFTkSuQmCC");}.ace_dark .ace_fold-widget.ace_end {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAH0lEQVQIW2P4//8/AxQ7wNjIAjDMgC4AxjCVKBirIAAF0kz2rlhxpAAAAABJRU5ErkJggg==");}.ace_dark .ace_fold-widget.ace_closed {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAFCAYAAACAcVaiAAAAHElEQVQIW2P4//+/AxAzgDADlOOAznHAKgPWAwARji8UIDTfQQAAAABJRU5ErkJggg==");}.ace_dark .ace_fold-widget:hover {box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);background-color: rgba(255, 255, 255, 0.1);}.ace_dark .ace_fold-widget:active {box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);}.ace_fold-widget.ace_invalid {background-color: #FFB4B4;border-color: #DE5555;}.ace_fade-fold-widgets .ace_fold-widget {-webkit-transition: opacity 0.4s ease 0.05s;transition: opacity 0.4s ease 0.05s;opacity: 0;}.ace_fade-fold-widgets:hover .ace_fold-widget {-webkit-transition: opacity 0.05s ease 0.05s;transition: opacity 0.05s ease 0.05s;opacity:1;}.ace_underline {text-decoration: underline;}.ace_bold {font-weight: bold;}.ace_nobold .ace_bold {font-weight: normal;}.ace_italic {font-style: italic;}.ace_error-marker {background-color: rgba(255, 0, 0,0.2);position: absolute;z-index: 9;}.ace_highlight-marker {background-color: rgba(255, 255, 0,0.2);position: absolute;z-index: 8;}.ace_br1 {border-top-left-radius    : 3px;}.ace_br2 {border-top-right-radius   : 3px;}.ace_br3 {border-top-left-radius    : 3px; border-top-right-radius:    3px;}.ace_br4 {border-bottom-right-radius: 3px;}.ace_br5 {border-top-left-radius    : 3px; border-bottom-right-radius: 3px;}.ace_br6 {border-top-right-radius   : 3px; border-bottom-right-radius: 3px;}.ace_br7 {border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-right-radius: 3px;}.ace_br8 {border-bottom-left-radius : 3px;}.ace_br9 {border-top-left-radius    : 3px; border-bottom-left-radius:  3px;}.ace_br10{border-top-right-radius   : 3px; border-bottom-left-radius:  3px;}.ace_br11{border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-left-radius:  3px;}.ace_br12{border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br13{border-top-left-radius    : 3px; border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br14{border-top-right-radius   : 3px; border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br15{border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;}
/*# sourceURL=ace/css/ace_editor.css */</style><style id="ace-tm">.ace-tm .ace_gutter {background: #f0f0f0;color: #333;}.ace-tm .ace_print-margin {width: 1px;background: #e8e8e8;}.ace-tm .ace_fold {background-color: #6B72E6;}.ace-tm {background-color: #FFFFFF;color: black;}.ace-tm .ace_cursor {color: black;}.ace-tm .ace_invisible {color: rgb(191, 191, 191);}.ace-tm .ace_storage,.ace-tm .ace_keyword {color: blue;}.ace-tm .ace_constant {color: rgb(197, 6, 11);}.ace-tm .ace_constant.ace_buildin {color: rgb(88, 72, 246);}.ace-tm .ace_constant.ace_language {color: rgb(88, 92, 246);}.ace-tm .ace_constant.ace_library {color: rgb(6, 150, 14);}.ace-tm .ace_invalid {background-color: rgba(255, 0, 0, 0.1);color: red;}.ace-tm .ace_support.ace_function {color: rgb(60, 76, 114);}.ace-tm .ace_support.ace_constant {color: rgb(6, 150, 14);}.ace-tm .ace_support.ace_type,.ace-tm .ace_support.ace_class {color: rgb(109, 121, 222);}.ace-tm .ace_keyword.ace_operator {color: rgb(104, 118, 135);}.ace-tm .ace_string {color: rgb(3, 106, 7);}.ace-tm .ace_comment {color: rgb(76, 136, 107);}.ace-tm .ace_comment.ace_doc {color: rgb(0, 102, 255);}.ace-tm .ace_comment.ace_doc.ace_tag {color: rgb(128, 159, 191);}.ace-tm .ace_constant.ace_numeric {color: rgb(0, 0, 205);}.ace-tm .ace_variable {color: rgb(49, 132, 149);}.ace-tm .ace_xml-pe {color: rgb(104, 104, 91);}.ace-tm .ace_entity.ace_name.ace_function {color: #0000A2;}.ace-tm .ace_heading {color: rgb(12, 7, 255);}.ace-tm .ace_list {color:rgb(185, 6, 144);}.ace-tm .ace_meta.ace_tag {color:rgb(0, 22, 142);}.ace-tm .ace_string.ace_regex {color: rgb(255, 0, 0)}.ace-tm .ace_marker-layer .ace_selection {background: rgb(181, 213, 255);}.ace-tm.ace_multiselect .ace_selection.ace_start {box-shadow: 0 0 3px 0px white;}.ace-tm .ace_marker-layer .ace_step {background: rgb(252, 255, 0);}.ace-tm .ace_marker-layer .ace_stack {background: rgb(164, 229, 101);}.ace-tm .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid rgb(192, 192, 192);}.ace-tm .ace_marker-layer .ace_active-line {background: rgba(0, 0, 0, 0.07);}.ace-tm .ace_gutter-active-line {background-color : #dcdcdc;}.ace-tm .ace_marker-layer .ace_selected-word {background: rgb(250, 250, 255);border: 1px solid rgb(200, 200, 250);}.ace-tm .ace_indent-guide {background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==") right repeat-y;}
/*# sourceURL=ace/css/ace-tm */</style><style>    .error_widget_wrapper {        background: inherit;        color: inherit;        border:none    }    .error_widget {        border-top: solid 2px;        border-bottom: solid 2px;        margin: 5px 0;        padding: 10px 40px;        white-space: pre-wrap;    }    .error_widget.ace_error, .error_widget_arrow.ace_error{        border-color: #ff5a5a    }    .error_widget.ace_warning, .error_widget_arrow.ace_warning{        border-color: #F1D817    }    .error_widget.ace_info, .error_widget_arrow.ace_info{        border-color: #5a5a5a    }    .error_widget.ace_ok, .error_widget_arrow.ace_ok{        border-color: #5aaa5a    }    .error_widget_arrow {        position: absolute;        border: solid 5px;        border-top-color: transparent!important;        border-right-color: transparent!important;        border-left-color: transparent!important;        top: -5px;    }</style><script src="./a8_q8_files/theme-cobalt.js.download"></script><script src="./a8_q8_files/mode-python.js.download"></script><script src="./a8_q8_files/mode-java.js.download"></script><style id="ace-cobalt">.ace-cobalt .ace_gutter {background: #011e3a;color: rgb(128,145,160)}.ace-cobalt .ace_print-margin {width: 1px;background: #555555}.ace-cobalt {background-color: #002240;color: #FFFFFF}.ace-cobalt .ace_cursor {color: #FFFFFF}.ace-cobalt .ace_marker-layer .ace_selection {background: rgba(179, 101, 57, 0.75)}.ace-cobalt.ace_multiselect .ace_selection.ace_start {box-shadow: 0 0 3px 0px #002240;}.ace-cobalt .ace_marker-layer .ace_step {background: rgb(127, 111, 19)}.ace-cobalt .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid rgba(255, 255, 255, 0.15)}.ace-cobalt .ace_marker-layer .ace_active-line {background: rgba(0, 0, 0, 0.35)}.ace-cobalt .ace_gutter-active-line {background-color: rgba(0, 0, 0, 0.35)}.ace-cobalt .ace_marker-layer .ace_selected-word {border: 1px solid rgba(179, 101, 57, 0.75)}.ace-cobalt .ace_invisible {color: rgba(255, 255, 255, 0.15)}.ace-cobalt .ace_keyword,.ace-cobalt .ace_meta {color: #FF9D00}.ace-cobalt .ace_constant,.ace-cobalt .ace_constant.ace_character,.ace-cobalt .ace_constant.ace_character.ace_escape,.ace-cobalt .ace_constant.ace_other {color: #FF628C}.ace-cobalt .ace_invalid {color: #F8F8F8;background-color: #800F00}.ace-cobalt .ace_support {color: #80FFBB}.ace-cobalt .ace_support.ace_constant {color: #EB939A}.ace-cobalt .ace_fold {background-color: #FF9D00;border-color: #FFFFFF}.ace-cobalt .ace_support.ace_function {color: #FFB054}.ace-cobalt .ace_storage {color: #FFEE80}.ace-cobalt .ace_entity {color: #FFDD00}.ace-cobalt .ace_string {color: #3AD900}.ace-cobalt .ace_string.ace_regexp {color: #80FFC2}.ace-cobalt .ace_comment {font-style: italic;color: #0088FF}.ace-cobalt .ace_heading,.ace-cobalt .ace_markup.ace_heading {color: #C8E4FD;background-color: #001221}.ace-cobalt .ace_list,.ace-cobalt .ace_markup.ace_list {background-color: #130D26}.ace-cobalt .ace_variable {color: #CCCCCC}.ace-cobalt .ace_variable.ace_language {color: #FF80E1}.ace-cobalt .ace_meta.ace_tag {color: #9EFFFF}.ace-cobalt .ace_indent-guide {background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAEklEQVQImWNgYGBgYHCLSvkPAAP3AgSDTRd4AAAAAElFTkSuQmCC) right repeat-y}
/*# sourceURL=ace/css/ace-cobalt */</style><style>.gc-bubbleDefault{background-color:transparent!important;text-align:left;padding:0!important;margin:0!important;border:0!important;table-layout:auto!important}.gc-reset{background-color:transparent!important;border:0!important;padding:0!important;margin:0!important;text-align:left}.pls-bubbleTop{border-bottom:1px solid #ccc!important}.pls-contentLeft,.pls-topTail,.pls-vertShimLeft{background-image:url(//ssl.gstatic.com/s2/oz/images/stars/po/bubblev1/border_3.gif)!important}.pls-topTail{background-repeat:repeat-x!important;background-position:bottom!important}.pls-vertShim{background-color:#fff!important;text-align:right}.tbl-grey .pls-vertShim{background-color:#f5f5f5!important}.pls-vertShimLeft{background-repeat:repeat-y!important;background-position:100%!important;height:4px}.pls-vertShimRight{height:4px}.pls-confirm-container .pls-vertShim{background-color:#fff3c2!important}.pls-contentWrap{background-color:#fff!important;position:relative!important;vertical-align:top}.pls-contentLeft{background-repeat:repeat-y;background-position:100%;vertical-align:top}.pls-dropRight{background-image:url(//ssl.gstatic.com/s2/oz/images/stars/po/bubblev1/bubbleDropR_3.png)!important;background-repeat:repeat-y!important;vertical-align:top}.pls-dropBL,.pls-dropTR .pls-dropBR,.pls-tailleft,.pls-vert,.pls-vert img{vertical-align:top}.pls-dropBottom{background-image:url(//ssl.gstatic.com/s2/oz/images/stars/po/bubblev1/bubbleDropB_3.png)!important;background-repeat:repeat-x!important;width:100%;vertical-align:top}.pls-topLeft{background:inherit!important;text-align:right;vertical-align:bottom}.pls-topRight{background:inherit!important;text-align:left;vertical-align:bottom}.pls-bottomLeft{background:inherit!important;text-align:right}.pls-bottomRight{background:inherit!important;text-align:left;vertical-align:top}.pls-tailbottom,.pls-tailleft,.pls-tailright,.pls-tailtop{display:none;position:relative}.pls-dropBL,.pls-dropBR,.pls-dropTR,.pls-tailbottom,.pls-tailleft,.pls-tailright,.pls-tailtop{background-image:url(//ssl.gstatic.com/s2/oz/images/stars/po/bubblev1/bubbleSprite_3.png)!important;background-repeat:no-repeat}.tbl-grey .pls-dropBL,.tbl-grey .pls-dropBR,.tbl-grey .pls-dropTR,.tbl-grey .pls-tailbottom,.tbl-grey .pls-tailleft,.tbl-grey .pls-tailright,.tbl-grey .pls-tailtop{background-image:url(//ssl.gstatic.com/s2/oz/images/stars/po/bubblev1/bubbleSprite-grey.png)!important}.pls-tailbottom{background-position:-23px 0}.pls-confirm-container .pls-tailbottom{background-position:-23px -10px}.pls-tailtop{background-position:-19px -20px}.pls-tailright{background-position:0 0}.pls-tailleft{background-position:-10px 0}.pls-tailtop{vertical-align:top}.gc-bubbleDefault td{line-height:0;font-size:0}.pls-tailbottom,.pls-topLeft img,.pls-topRight img{vertical-align:bottom}.bubbleDropTR,.pls-bottomLeft,.pls-bottomLeft img,.pls-dropBottom img,.pls-dropBottomL img,.pls-dropBottomR img{vertical-align:top}.pls-dropTR{background-position:0 -22px}.pls-dropBR{background-position:0 -27px}.pls-dropBL{background-position:0 -16px}.pls-spacerbottom,.pls-spacerleft,.pls-spacerright,.pls-spacertop{position:static!important}.pls-spinner{bottom:0;position:absolute;left:0;margin:auto;right:0;top:0}</style></head>

<body class=" resource theme1" style="">
   
   <header>
         <nav>
            <div class="nav-wrapper page-scrolled">
               <div class="container med row  site-nav">
                  <a href="https://www.pepcoding.com/" class="brand-logo small">
                     <img class="logo" src="./a8_q8_files/logo2.png" alt="logo">
                  </a>
                  <div class="hide-on-med-and-down nav-breadcrumb">
                        <a class="breadcrumb  " data-target="ddls0" href="https://www.pepcoding.com/resources/">
                           home
                        </a>
                        <a class="breadcrumb  " data-target="ddls1" href="https://www.pepcoding.com/resources/online-java-foundation/">
                           online-java-foundation
                        </a>
                        <a class="breadcrumb  " data-target="ddls2" href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/">
                           getting-started
                        </a>
                        <a class="breadcrumb  " data-target="ddls3" href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/">
                           rotate-a-number-official
                        </a>
                  </div>
                        <a href="https://classroom.pepcoding.com/myClassroom" class="class-mode">My ClassRoom </a>
                                    
                     <a class="dropdown-trigger dashboard-burger" href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion#" data-target="ddlFeatures">
                        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" width="1em" height="1em" style="-ms-transform: rotate(360deg); -webkit-transform: rotate(360deg); transform: rotate(360deg);" preserveAspectRatio="xMidYMid meet" viewBox="0 0 384 384">
                           <path d="M0 384v-43h384v43H0zm0-277l85 85l-85 85V107zm171 192v-43h213v43H171zM0 0h384v43H0V0zm171 128V85h213v43H171zm0 85v-42h213v42H171z" fill="currentColor"></path>
                        </svg>
                     </a><ul id="ddlFeatures" class="dropdown-content" tabindex="0">
                     <li tabindex="0">
                        <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion#" class=" setting sidenav-trigger theme-cutomizer-trigger no-margin" data-target="editor-support-out" id="135086">
                           <div class="row  col l12 no-padding no-margin" style="height: 100%;display: flex;flex-direction: row;align-items: center;justify-content: flex-end;">
                              <i class="fa fa-code" aria-hidden="true"></i>
                              <span class="col l8 s8 m8 lp-dropdown">Editor</span>
                           </div>
                        </a>
                     </li>
                  </ul>
                              <div class="changeTheme">
                                          <i class="fa fa-sun-o  dropdown-trigger" href="#changeSiteTheme" style="    height: inherit;
                                             line-height: inherit;"></i><ul id="changeSiteTheme" class="dropdown-content changeSiteTheme" tabindex="0">
                                         <li tabindex="0">
                                             <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion#" onclick="siteThemeSelect(&#39;theme1&#39;)">
                                                <div class="row   ">
                                                     <div class="col l1  heart theme1"></div> 
                                                  <div class="col l4">Theme1</div>
                                                </div>
                                             </a>
                                          </li>
                                          
                                         <li tabindex="0">
                                             <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion#" onclick="siteThemeSelect(&#39;theme2&#39;)">
                                                <div class="row   ">
                                                     <div class="col l1  heart theme2"></div> 
                                                  <div class="col l4">Theme2</div>
                                                </div>
                                             </a>
                                          </li>
                                           <li tabindex="0">
                                             <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion#" onclick="siteThemeSelect(&#39;theme3&#39;)">
                                                <div class="row   ">
                                                     <div class="col l1  heart theme3"></div> 
                                                  <div class="col l4">Theme3</div>
                                                </div>
                                             </a>
                                          </li>
                                           <li tabindex="0">
                                             <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion#" onclick="siteThemeSelect(&#39;theme4&#39;)">
                                                <div class="row   ">
                                                     <div class="col l1  heart theme4"></div> 
                                                  <div class="col l4">Theme4</div>
                                                </div>
                                             </a>
                                          </li>
                                       </ul>
                               </div>
                                                  <a class="dropdown-trigger dashboard-user" href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion#" data-target="ddlUserProfile">
                        <i class="svg-user svg-header"></i>
                     </a><ul id="ddlUserProfile" class="dropdown-content" tabindex="0" style="">
                    <li tabindex="0">
                      <a href="https://www.pepcoding.com/profile" class="setting">
                        <div class="row  col l12" style="height: 100%;padding: 0px;margin: 0px;display: flex;flex-direction: row;align-items: center;justify-content: flex-end;">
                          <i class="col l4 s2 m2 svg-user svg-header"></i>
                          <span class="col l8 s8 m8 lp-dropdown">Profile</span>
                        </div>
                      </a>
                    </li>
                    <li tabindex="0">
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion#" class="setting" onclick="PEP.Utilities.signOut();">
                          <div class="row  col l12" style="height: 100%;padding: 0px;margin: 0px;display: flex;flex-direction: row;align-items: center;justify-content: flex-end;">
                            <i class="col l4 s2 m2 svg-logout svg-header"></i>
                          <span class="col l8 s8 m8 lp-dropdown">Logout</span>
                        </div>
                      </a>
                    </li>
                  </ul>
               </div>
            </div>
         </nav>
   </header>
   <main>
      <div id="siteOverlay" class="loader-overlay hide">
      </div>
      <div id="siteLoader" class="loader hide">
         <div class="preloader-wrapper active">
            <div class="spinner-layer spinner-red-only">
               <div class="circle-clipper left">
                  <div class="circle"></div>
               </div>
               <div class="gap-patch">
                  <div class="circle"></div>
               </div>
               <div class="circle-clipper right">
                  <div class="circle"></div>
               </div>
            </div>
         </div>
      </div>
      <div id="siteOverlay-nados" class="loader-overlay-nados hide"></div>
      <div id="siteLoader-nados" class="load-container d-flex flex-center valign-wrapper hide">
         <h2 class="center loader-h2 bolder white-text">Redirecting to <br> NADOS
         <div class="timmer-nados"></div></h2>
         <div class="loader-nados"></div>
      </div>
      <input type="hidden" id="isShowDoubtSupport" value="false">
         <input type="hidden" id="tawkKey" value="5e1ef6557e39ea1242a4b602">
      <div class="container full  ">


    <div class="section full no-padding">
        <div class="row" style="display: flex; flex-flow: column;">
            <div id="side-open-nav" class="sidenav sidenav-fixed sidenav-res search-nav row  " style="transform: translateX(0px);">
            
              <div class="col l1 s1 m1 no-padding">
            
                <span class="sidenav-icon open">
            
            
                  <div id="toggleResourceNav" class=" mobile-nav menu-ico ">
                    <span class="side-nav"></span>
                    <span class="side-nav"></span>
                    <span class="side-nav"></span>
                  </div>
            
                </span>
            
                <span class="hide " style="margin-top:200px; position: absolute;">
            
                  <div id="resourceNotice " class="resource-notice">
            
                    <i class="fa fa-flag-o " aria-hidden="true"></i>
                  </div>
            
                </span>
            
              </div>
            
              <div class="col l11 s11 m11 ">
                <ul class="row col l12 s12 m12  no-padding" style="    height: 8vh;">
            
                  <li class="search-container">
                    <i class="search-icon fa fa-search"></i>
                    <input id="searchBox" type="text" placeholder=" search" class=" row col l9 s9 autocomplete search searchBox">
            
                  </li>
            
                </ul>
            
            
                <ul class="row col l12 s12 m12  no-padding" style="    height: 92vh;
                overflow-y: scroll;">
            
            
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/how_to_print_in_java/topic">
            
                      
            
            
            
                      <span title="How To Print In Java" class="bold  ">
            
            
            
            
            
            
            
                        <i class="svg-resources svg-topic"></i>
            
            
                        How To Print In Java
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/print_z_in_java/topic">
            
                      
            
            
            
                      <span title="Print Z In Java" class="bold  ">
            
            
            
            
            
            
            
                        <i class="svg-resources svg-topic"></i>
            
            
                        Print Z In Java
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/print-z-official/ojquestion">
            
                      
            
            
            
                      <span title="Print Z" class="bold  ">
            
            
            
            
            
            
                        <i class="fa fa-code " style="padding-right:4%"></i>
            
            
            
                        Print Z
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/variables_in_java_official/topic">
            
                      
            
            
            
                      <span title="Variables In Java" class="bold  ">
            
            
            
            
            
            
            
                        <i class="svg-resources svg-topic"></i>
            
            
                        Variables In Java
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/variables-official/video">
            
                      
            
            
            
                      <span title="Variables" class="bold  ">
            
            
            
            
            
            
            
            
                        <i class="svg-resources svg-video"></i>
            
                        Variables
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/variables-in-java-mcq-official/mcq">
            
                      
            
            
            
                      <span title="Variables In Java" class="bold  ">
            
            
            
            
            
            
            
            
                        <i class="svg-resources svg-mcq"></i>
            
                        Variables In Java
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/grading_system/topic">
            
                      
            
            
            
                      <span title="Grading System" class="bold  ">
            
            
            
            
            
            
            
                        <i class="svg-resources svg-topic"></i>
            
            
                        Grading System
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/grading-system-official/ojquestion">
            
                      
            
            
                      
            
                      <span title="Grading System" class="bold  ">
            
            
            
            
            
            
                        <i class="fa fa-code " style="padding-right:4%"></i>
            
            
            
                        Grading System
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/loops_official/topic">
            
                      
            
            
            
                      <span title="Loops" class="bold  ">
            
            
            
            
            
            
            
                        <i class="svg-resources svg-topic"></i>
            
            
                        Loops
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/loops-official/video">
            
                      
            
            
            
                      <span title="Loops" class="bold  ">
            
            
            
            
            
            
            
            
                        <i class="svg-resources svg-video"></i>
            
                        Loops
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/increment-operators-official/mcq">
            
                      
            
            
            
                      <span title="Increment Operators" class="bold  ">
            
            
            
            
            
            
            
            
                        <i class="svg-resources svg-mcq"></i>
            
                        Increment Operators
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/take_input/topic">
            
                      
            
            
            
                      <span title="Take Input" class="bold  ">
            
            
            
            
            
            
            
                        <i class="svg-resources svg-topic"></i>
            
            
                        Take Input
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/conditionals-official/video">
            
                      
            
            
            
                      <span title="Conditionals" class="bold  ">
            
            
            
            
            
            
            
            
                        <i class="svg-resources svg-video"></i>
            
                        Conditionals
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/take-input-official/video">
            
                      
            
            
            
                      <span title="Take Input" class="bold  ">
            
            
            
            
            
            
            
            
                        <i class="svg-resources svg-video"></i>
            
                        Take Input
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/is_a_number_prime/topic">
            
                      
            
            
            
                      <span title="Is A Number Prime" class="bold  ">
            
            
            
            
            
            
            
                        <i class="svg-resources svg-topic"></i>
            
            
                        Is A Number Prime
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/is-number-prime-official/ojquestion">
            
                      
            
            
                      
            
                      <span title="Is A Number Prime" class="bold  ">
            
            
            
            
            
            
                        <i class="fa fa-code " style="padding-right:4%"></i>
            
            
            
                        Is A Number Prime
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/primes_till_n/topic">
            
                      
            
            
            
                      <span title="Primes Till N" class="bold  ">
            
            
            
            
            
            
            
                        <i class="svg-resources svg-topic"></i>
            
            
                        Primes Till N
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/what_are_conditional_statements/topic">
            
                      
            
            
            
                      <span title="What Are Conditional Statements" class="bold  ">
            
            
            
            
            
            
            
                        <i class="svg-resources svg-topic"></i>
            
            
                        What Are Conditional Statements
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/print-all-primes-till-n-official/ojquestion">
            
                      
            
            
            
                      <span title="Print All Primes Till N" class="bold  ">
            
            
            
            
            
            
                        <i class="fa fa-code " style="padding-right:4%"></i>
            
            
            
                        Print All Primes Till N
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/print_fibonacci_numbers_till_n/topic">
            
                      
            
            
            
                      <span title="Print Fibonacci Numbers Till N" class="bold  ">
            
            
            
            
            
            
            
                        <i class="svg-resources svg-topic"></i>
            
            
                        Print Fibonacci Numbers Till N
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/fibonacci-till-n-official/ojquestion">
            
                      
            
            
            
                      <span title="Print Fibonacci Numbers Till N" class="bold  ">
            
            
            
            
            
            
                        <i class="fa fa-code " style="padding-right:4%"></i>
            
            
            
                        Print Fibonacci Numbers Till N
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/counting_digits_in_a_number/topic">
            
                      
            
            
            
                      <span title="Count Digits In A Number" class="bold  ">
            
            
            
            
            
            
            
                        <i class="svg-resources svg-topic"></i>
            
            
                        Count Digits In A Number
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/count-digits-official/ojquestion">
            
                      
            
            
            
                      <span title="Count Digits In A Number" class="bold  ">
            
            
            
            
            
            
                        <i class="fa fa-code " style="padding-right:4%"></i>
            
            
            
                        Count Digits In A Number
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/digits-of-a-number-official/ojquestion">
            
                      
            
            
            
                      <span title="Digits Of A Number" class="bold  ">
            
            
            
            
            
            
                        <i class="fa fa-code " style="padding-right:4%"></i>
            
            
            
                        Digits Of A Number
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/digits_of_a_number/topic">
            
                      
            
            
            
                      <span title="Digits Of A Number" class="bold  ">
            
            
            
            
            
            
            
                        <i class="svg-resources svg-topic"></i>
            
            
                        Digits Of A Number
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/how-to-print-in-java-official/video">
            
                      
            
            
            
                      <span title="How To Print In Java" class="bold  ">
            
            
            
            
            
            
            
            
                        <i class="svg-resources svg-video"></i>
            
                        How To Print In Java
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/reverse_a_number/topic">
            
                      
            
            
            
                      <span title="Reverse A Number" class="bold  ">
            
            
            
            
            
            
            
                        <i class="svg-resources svg-topic"></i>
            
            
                        Reverse A Number
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/reverse-a-number-official/ojquestion">
            
                      
            
            
            
                      <span title="Reverse A Number" class="bold  ">
            
            
            
            
            
            
                        <i class="fa fa-code " style="padding-right:4%"></i>
            
            
            
                        Reverse A Number
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/inverse_of_number/topic">
            
                      
            
            
            
                      <span title="Inverse Of A Number" class="bold  ">
            
            
            
            
            
            
            
                        <i class="svg-resources svg-topic"></i>
            
            
                        Inverse Of A Number
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/inverse-of-a-number-official/ojquestion">
            
                      
            
            
            
                      <span title="Inverse Of A Number" class="bold  ">
            
            
            
            
            
            
                        <i class="fa fa-code " style="padding-right:4%"></i>
            
            
            
                        Inverse Of A Number
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate_a_number/topic">
            
                      
            
            
            
                      <span title="Rotate A Number" class="bold  ">
            
            
            
            
            
            
            
                        <i class="svg-resources svg-topic"></i>
            
            
                        Rotate A Number
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow active">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion">
            
                      
            
            
            
                      <span title="Rotate A Number" class="bold  ">
            
            
            
            
            
            
                        <i class="fa fa-code " style="padding-right:4%"></i>
            
            
            
                        Rotate A Number
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/gcd_and_lcm/topic">
            
                      
            
            
            
                      <span title="Gcd &amp; Lcm" class="bold  ">
            
            
            
            
            
            
            
                        <i class="svg-resources svg-topic"></i>
            
            
                        Gcd &amp; Lcm
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/gcd-and-lcm-official/ojquestion">
            
                      
            
            
            
                      <span title="Gcd And Lcm" class="bold  ">
            
            
            
            
            
            
                        <i class="fa fa-code " style="padding-right:4%"></i>
            
            
            
                        Gcd And Lcm
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/prime_factorization_of_a_number/topic">
            
                      
            
            
            
                      <span title="Prime Factorization Of A Number" class="bold  ">
            
            
            
            
            
            
            
                        <i class="svg-resources svg-topic"></i>
            
            
                        Prime Factorization Of A Number
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/prime-factorization-official/ojquestion">
            
                      
            
            
            
                      <span title="Prime Factorization Of A Number" class="bold  ">
            
            
            
            
            
            
                        <i class="fa fa-code " style="padding-right:4%"></i>
            
            
            
                        Prime Factorization Of A Number
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/pythagorean_triplet/topic">
            
                      
            
            
            
                      <span title="Pythagorean Triplet" class="bold  ">
            
            
            
            
            
            
            
                        <i class="svg-resources svg-topic"></i>
            
            
                        Pythagorean Triplet
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/the_curious_case_of_benjamin_bulbs/topic">
            
                      
            
            
            
                      <span title="The Curious Case Of Benjamin Bulbs" class="bold  ">
            
            
            
            
            
            
            
                        <i class="svg-resources svg-topic"></i>
            
            
                        The Curious Case Of Benjamin Bulbs
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/benjamin-bulbs-official/ojquestion">
            
                      
            
            
            
                      <span title="The Curious Case Of Benjamin Bulbs" class="bold  ">
            
            
            
            
            
            
                        <i class="fa fa-code " style="padding-right:4%"></i>
            
            
            
                        The Curious Case Of Benjamin Bulbs
                      </span>
                    </a>
                  </li>
            
                  <li class=" searchRow">
                    
                    
                    
            
                      <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/increment_operators_mcq/topic">
            
                      
            
            
            
                      <span title="Increment Operators MCQ" class="bold  ">
            
            
            
            
            
            
            
                        <i class="svg-resources svg-topic"></i>
            
            
                        Increment Operators MCQ
                      </span>
                    </a>
                  </li>
            
                  <li></li>
                  <li></li>
                </ul>
              </div>
            
            </div>            
            <div id="resource-card" class="resource-card no-margin flex  ">
                    <div class="  no-margin no-padding" id="splitQuestion" style="flex-basis: calc(50% - 5px);">
                        <div class="card-tabs  header">
                            <ul id="resourceNavTabs" class="tabs tab-border valign-wrapper    tabs-fixed-width   " style="height:100%">

                            <li class="tab bold queTab active"><a class="active" action="showQuestion" href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion#resource"><i class="fa fa-file-code-o" aria-hidden="true"></i> &nbsp; Question</a>
                                </li>

                            <li class="tab bold historyTab"><a action="showHistory" href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion#history"><i class="fa fa-history" aria-hidden="true"></i> &nbsp; History </a>
                                </li>
                                <input type="hidden" id="marks" value="10">

                                <li class="tab bold editorTab">
                                    <a class="lang" action="showSolution" href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion#solutionContainer">
                                        <div><i class="fa fa-flask" aria-hidden="true"></i> &nbsp; Solution</div>
                                    </a>

                                </li>
                            <li class="tab bold modalTab"><a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion#statsContainer" action="showStats"> <i class="fa fa-hourglass-start" aria-hidden="true"></i> &nbsp;
                                        Stats</a></li>

                                <i class="fa fa-arrows-alt code-fullscreen  " id="fullScreenQuestion"></i>


                            <li class="indicator" style="left: 0px; right: 982px;"></li></ul>
                        </div>

                        <div id="resourceContent" style="margin:0px 0px 10px 50px;">
                            <div id="resource" class="resource-content card-content no-padding active row" style="margin-right:0px;">
                                <div class="col  l12 s12 m8 ">
                                    <h1 class="row   bold" style="margin-top:30px;font-size:1.3rem">
                                        <div class=" col l10 s12  ">Rotate A Number</div>
                                        <div class="col l2 s2 m2   ">
                                            <div class="follow no-margin  " style="margin:0px">
                                                <img class="course-icon-svg" height="20" width="20" alt="" src="./a8_q8_files/share.svg">
                                                <span class="social-icons-on-hover ">
                                                    <a href="https://www.facebook.com/sharer/sharer.php?u=https://www.pepcoding.com/resources" class="" target="_blank">
                                                        <svg height="10" viewBox="0 0 24 24" width="10">
                                                            <path d="m15.997 3.985h2.191v-3.816c-.378-.052-1.678-.169-3.192-.169-6.932 0-5.046 7.85-5.322 9h-3.487v4.266h3.486v10.734h4.274v-10.733h3.345l.531-4.266h-3.877c.188-2.824-.761-5.016 2.051-5.016z" fill="#3b5999"></path>
                                                        </svg>
                                                    </a>
                                                    <a href="https://www.linkedin.com/sharing/share-offsite/?url=https://www.pepcoding.com/resources" class="" target="_blank">
                                                        <svg height="10" viewBox="0 0 24 24" width="10">
                                                            <g fill="#0077b5">
                                                                <path d="m23.994 24v-.001h.006v-8.802c0-4.306-.927-7.623-5.961-7.623-2.42 0-4.044 1.328-4.707 2.587h-.07v-2.185h-4.773v16.023h4.97v-7.934c0-2.089.396-4.109 2.983-4.109 2.549 0 2.587 2.384 2.587 4.243v7.801z"></path>
                                                                <path d="m.396 7.977h4.976v16.023h-4.976z"></path>
                                                                <path d="m2.882 0c-1.591 0-2.882 1.291-2.882 2.882s1.291 2.909 2.882 2.909 2.882-1.318 2.882-2.909c-.001-1.591-1.292-2.882-2.882-2.882z"></path>
                                                            </g>
                                                        </svg>
                                                    </a>
                                                </span>
                                            </div>
                                        </div>
                                    </h1>
                                    <div class="row">
                                        <div class="col l8 s6 m3">
                                            <span class="badge easy  login-badge card card-light" style="">
                                                <i class=" fa fa-circle"> </i>easy
                                            </span>
                                        </div>
                                        <div class="col l4 s6 m6  "> 
                                
                                            <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate_a_number/topic" class="prev-link"> <i class=" fa fa-chevron-left red-text"> </i>&nbsp;&nbsp;Prev </a>
                                
                                
                                
                                            <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/gcd_and_lcm/topic" class="next-link"> <i class=" fa fa-chevron-right red-text"> </i>&nbsp;&nbsp;Next </a>
                                
                                
                                        </div>
                                    </div>
                                    <div class="row divider"></div>
                                        <div class="card hide ">
                                            
                                             
                                            <p class="text-ellipses no-margin" style="-webkit-line-clamp:2;">
                                                </p><h4 class="bold">Try First, Check Solution later</h4>1. You should first read the question and watch the question video.<br>2. Think of a solution approach, then try and submit the question on editor tab.<br>3. We strongly advise you to watch the solution video for prescribed approach.<br>
                                            <p></p>
                                        </div>
                                    <pre class=" card">1. You are given two numbers n and k. You are required to rotate n, k times to the right. If k is positive, rotate to the right i.e. remove rightmost digit and make it leftmost. Do the reverse for negative value of k. Also k can have an absolute value larger than number of digits in n.<br>2. Take as input n and k.<br>3. Print the rotated number.<br>4. Note - Assume that the number of rotations will not cause leading 0's in the result. e.g. such an input will not be given<br>   n = 12340056<br>   k = 3<br>   r = 05612340</pre>
                                    <span class="pre-heading   bolder"> Input Format</span>
                                    <pre class="card">"n" where n is any integer.<br>"K" where k is any integer.</pre>
                                    <span class="pre-heading  bolder">Output Format</span>
                                    <pre class="card">"r", the rotated number</pre>
                                    <span class="pre-heading  bolder">Question Video</span>
                                    <div class="question-text-video card ">
                                            
                                            <iframe class="card-content no-padding" src="./a8_q8_files/ysMHtDIlU0c.html" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen=""></iframe>
                                             <input id="videoId" type="hidden" value="https://www.youtube.com/embed/ysMHtDIlU0c?rel=0">
                                            <div class="card-content no-padding">
                                                    <div id="___ytsubscribe_0" style="text-indent: 0px; margin: 0px; padding: 0px; background: transparent; border-style: none; float: none; line-height: normal; font-size: 1px; vertical-align: baseline; display: inline-block; width: 122px; height: 24px;"><iframe ng-non-bindable="" frameborder="0" hspace="0" marginheight="0" marginwidth="0" scrolling="no" style="position: static; top: 0px; width: 122px; margin: 0px; border-style: none; left: 0px; visibility: visible; height: 24px;" tabindex="0" vspace="0" width="100%" id="I0_1673971899828" name="I0_1673971899828" src="./a8_q8_files/subscribe_embed.html" data-gapiattached="true"></iframe></div>
                                                    <i class="fa fa-thumbs-up likeVideo" aria-hidden="true" style="transform: scale(-2,2);margin:7px"></i>
                                                    <button class="btn comment modal-trigger" data-target="videoComment" style="margin: 7px;">Comment</button>
                                                        <div id="videoComment" class="modal" style="z-index: 1013;">
                                                            <div class="modal-content">
                                                                <div class="row">
                                                                    <div class="row no-margin">
                                                                        <h1 class="col l10 s10 m10 center no-margin">Comment
                                                                        </h1>
                                                                        <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion#!" class="col l2 s2 m2 modal-close waves-effect waves-green"><i class="svg-close svg-header"></i></a>
                                                                    </div>
                                                                    <textarea id="commentContent" required="">                                                        
                                                                    </textarea>
                                                                    <button class="btn" id="postYoutubeComment">Post Comment</button>
                                                                </div>
                                                            </div>
                                                        </div>        </div>
                                    
                                    
                                        </div>        <span class=" pre-heading  bolder">Constraints</span>
                                        <pre class="card">1 &lt;= n &lt; 10^9<br>-10^9 &lt; k &lt; 10^9</pre>
                                        <span class="pre-heading  bolder question-text-sample-input">Sample Input</span>
                                        <pre class="card question-text-sample-input">562984<br>2</pre>
                                    <input type="hidden" id="sampleInput" value="562984&lt;br/&gt;2">
                                        <span class="pre-heading  bolder question-text-sample-output">Sample Output</span>
                                        <pre class="card question-text-sample-input">845629</pre>
                                    <input type="hidden" id="sampleOutput" value="845629">
                                    <br>
                                    <br>
                                    <ul class="  collapsible cl2 row " id="editorial">
                                            <li class="editorial col l12 s12 m12 ">
                                                <div class="collapsible-header "><i class="  fa fa-plus fa-str-bg1 s1 "></i>Editorial</div>
                                                <div class="collapsible-body"><p><i>"The most important property of a program is whether it accomplishes the intention of its user."</i></p><p><b><u>Question:</u></b></p><ol><li>You are given two numbers n and k. You are required to rotate n, k times to the right. If k is positive, rotate to the right i.e. remove the rightmost digit and make it leftmost. Do the reverse for the negative value of k. Also, k can have an absolute value larger than a number of digits in n.</li><li>Take as input n and k.</li><li>Print the rotated number.</li><li>Note - Assume that the number of rotations will not cause leading 0's in the result. e.g. such input will not be given</li></ol><p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; n = 12340056</p><p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; k = 3</p><p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; r = 05612340</p><p><b><u>Input format:</u></b></p><p>"n" where n is an integer.</p><p>"K" where k is an integer.</p><p><b><u>Output format:</u></b></p><p>"r", the rotated number</p><p><b><u>Constraints:</u></b></p><p>1 &lt;= n &lt; 10^9</p><p>-10^9 &lt; k &lt; 10^9</p><p>In this question, we have to transform the given number 'n' in the following manner to get the rotated number 'r' : (here n = <b>25398</b>)</p><p></p><p><img src="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion"><img src="./a8_q8_files/rotate_a_number_1.PNG"></p><p><b><u>Solution Approach:</u></b></p><p>There are three cases to be handled in this problem:</p><ol><li>The positive value of k</li><li>The negative value of k</li><li>Value of k larger than the number of digits in n</li></ol><p>The major portion of the problem will be solved by the first case and on a few modifications; the remaining two cases can be accommodated. We will focus on the first case to start.</p><p></p><p><img src="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion"><img src="./a8_q8_files/rotate_a_number_2.PNG"></p><p>Let us take another example of <b>273516</b></p><p><b></b></p><p><b><img src="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion"><img src="./a8_q8_files/rotate_a_number_3.PNG"></b></p><p>Rotating by +2 will give us <b>162735.</b> So the question now arises that how to decide the divisor value and the multiplier value.</p><p>This is simple to analyze as we know the value of k is 2 in the cases and we divide by 100 to get the remainder. Observe 100 = 10^2 = 10^k.</p><p>Similarly, looking at the multiplier 10000 = 10 ^(6-2) = 10^(number of digits-k) = 10^4.</p><p>Programming implementation for the same will be:</p><div class="codeEditor   " id="6GA93"><div class="code-container  editorial row">


    <div class="col s12 l12 m12 d-flex editorOptions row no-margin  ">

        <div class="item" style="width: 14%;">
            <!-- <select id="tutorial_editor_6GA93_lang_select" disabled class="code-lang-select white-text" style="width:100px"
                title="Select Language">
            </select> -->
            <p style="text-transform: capitalize;" class=" ">java</p>
        </div>
   
        <div class="item">
            <select id="tutorial_editor_6GA93_font_select" title="Select Editor Font Size" class="code-font-select   ">
            <option value="12px">12px</option><option value="13px">13px</option><option value="14px">14px</option><option value="15px">15px</option><option value="16px">16px</option><option value="17px">17px</option><option value="18px">18px</option></select>
            <!-- <i class="fa fa-text-height code-font-select  "></i> -->
        </div>
       
        
        <div class="item">
            <i id="tutorial_editor_6GA93_full_screen" class="fa fa-arrows-alt code-fullscreen  " aria-hidden="true" title="FullScreen"></i>
        </div>
         
    </div>
    <div class="col l12 s12 m12 editor ace_editor ace-cobalt ace_dark" id="tutorial_editor_6GA93" style="font-size: 12px; font-family: monospace;"><textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0;"></textarea><div class="ace_gutter"><div class="ace_layer ace_gutter-layer ace_folding-enabled"></div><div class="ace_gutter-active-line" style="display: none;"></div></div><div class="ace_scroller"><div class="ace_content"><div class="ace_layer ace_print-margin-layer"><div class="ace_print-margin" style="left: 4px; visibility: hidden;"></div></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_text-layer" style="padding: 0px 4px;"></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_cursor-layer ace_hidden-cursors"><div class="ace_cursor"></div></div></div></div><div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 22px;"><div class="ace_scrollbar-inner" style="width: 22px;"></div></div><div class="ace_scrollbar ace_scrollbar-h" style="display: none; height: 22px;"><div class="ace_scrollbar-inner" style="height: 22px;"></div></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;"><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;"></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div></div></div>

   
     <span class="pre-heading  bolder">Output of Above Code</span>
    <pre class="output col l12 s12 m12"></pre>
</div>
</div><p></p><p>Now, this code will work for only the first mentioned case.</p><p><b><u>To accommodate the remaining cases, we make an important observation:</u></b></p><p></p><p><img src="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion"><img src="./a8_q8_files/rotate_a_number_4.PNG"></p><p></p><p><b><u>So, implementing the same in code:</u></b></p><div class="codeEditor   " id="cLvRo"><div class="code-container  editorial row">


    <div class="col s12 l12 m12 d-flex editorOptions row no-margin  ">

        <div class="item" style="width: 14%;">
            <!-- <select id="tutorial_editor_cLvRo_lang_select" disabled class="code-lang-select white-text" style="width:100px"
                title="Select Language">
            </select> -->
            <p style="text-transform: capitalize;" class=" ">java</p>
        </div>
   
        <div class="item">
            <select id="tutorial_editor_cLvRo_font_select" title="Select Editor Font Size" class="code-font-select   ">
            <option value="12px">12px</option><option value="13px">13px</option><option value="14px">14px</option><option value="15px">15px</option><option value="16px">16px</option><option value="17px">17px</option><option value="18px">18px</option></select>
            <!-- <i class="fa fa-text-height code-font-select  "></i> -->
        </div>
       
        
        <div class="item">
            <i id="tutorial_editor_cLvRo_full_screen" class="fa fa-arrows-alt code-fullscreen  " aria-hidden="true" title="FullScreen"></i>
        </div>
         
    </div>
    <div class="col l12 s12 m12 editor ace_editor ace-cobalt ace_dark" id="tutorial_editor_cLvRo" style="font-size: 12px; font-family: monospace;"><textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0;"></textarea><div class="ace_gutter"><div class="ace_layer ace_gutter-layer ace_folding-enabled"></div><div class="ace_gutter-active-line" style="display: none;"></div></div><div class="ace_scroller"><div class="ace_content"><div class="ace_layer ace_print-margin-layer"><div class="ace_print-margin" style="left: 4px; visibility: hidden;"></div></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_text-layer" style="padding: 0px 4px;"></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_cursor-layer ace_hidden-cursors"><div class="ace_cursor"></div></div></div></div><div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 22px;"><div class="ace_scrollbar-inner" style="width: 22px;"></div></div><div class="ace_scrollbar ace_scrollbar-h" style="display: none; height: 22px;"><div class="ace_scrollbar-inner" style="height: 22px;"></div></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;"><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;"></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div></div></div>

   
     <span class="pre-heading  bolder">Output of Above Code</span>
    <pre class="output col l12 s12 m12"></pre>
</div>
</div><p></p><p>Moving on to the third and final case as to if we are given a k greater than the number of digits in the number.</p><p></p><p><img src="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion"><img src="./a8_q8_files/rotate_a_number_5.PNG"></p><p></p><p>If k is a multiple of a number of digits (either + or -), then the rotation has no effect.</p><p>So we divide k and store in k the remainder we get by dividing it with the number of digits.</p><p>This will store in k the number of rotations needed to be done.</p><p>We will write this before we deal with the k for negative values because the remainder can be negative and then it should be handled.</p><p>The final code should be:</p><div class="codeEditor   " id="qLWhf"><div class="code-container  editorial row">


    <div class="col s12 l12 m12 d-flex editorOptions row no-margin  ">

        <div class="item" style="width: 14%;">
            <!-- <select id="tutorial_editor_qLWhf_lang_select" disabled class="code-lang-select white-text" style="width:100px"
                title="Select Language">
            </select> -->
            <p style="text-transform: capitalize;" class=" ">java</p>
        </div>
   
        <div class="item">
            <select id="tutorial_editor_qLWhf_font_select" title="Select Editor Font Size" class="code-font-select   ">
            <option value="12px">12px</option><option value="13px">13px</option><option value="14px">14px</option><option value="15px">15px</option><option value="16px">16px</option><option value="17px">17px</option><option value="18px">18px</option></select>
            <!-- <i class="fa fa-text-height code-font-select  "></i> -->
        </div>
       
        
        <div class="item">
            <i id="tutorial_editor_qLWhf_full_screen" class="fa fa-arrows-alt code-fullscreen  " aria-hidden="true" title="FullScreen"></i>
        </div>
         
    </div>
    <div class="col l12 s12 m12 editor ace_editor ace-cobalt ace_dark" id="tutorial_editor_qLWhf" style="font-size: 12px; font-family: monospace;"><textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0;"></textarea><div class="ace_gutter"><div class="ace_layer ace_gutter-layer ace_folding-enabled"></div><div class="ace_gutter-active-line" style="display: none;"></div></div><div class="ace_scroller"><div class="ace_content"><div class="ace_layer ace_print-margin-layer"><div class="ace_print-margin" style="left: 4px; visibility: hidden;"></div></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_text-layer" style="padding: 0px 4px;"></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_cursor-layer ace_hidden-cursors"><div class="ace_cursor"></div></div></div></div><div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 22px;"><div class="ace_scrollbar-inner" style="width: 22px;"></div></div><div class="ace_scrollbar ace_scrollbar-h" style="display: none; height: 22px;"><div class="ace_scrollbar-inner" style="height: 22px;"></div></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;"><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;"></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div></div></div>

   
     <span class="pre-heading  bolder">Output of Above Code</span>
    <pre class="output col l12 s12 m12"></pre>
</div>
</div><p><b><u>Sample input value:</u></b></p><p>25378 (n)</p><p>2 (k)</p><p><b><u>Output: (r)</u></b></p><p></p><p><img src="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion"><img src="./a8_q8_files/rotate_a_number_6.PNG"></p><p><b><u>Alternative Programming Style:</u></b></p><div class="codeEditor   " id="HMW5e"><div class="code-container  editorial row">


    <div class="col s12 l12 m12 d-flex editorOptions row no-margin  ">

        <div class="item" style="width: 14%;">
            <!-- <select id="tutorial_editor_HMW5e_lang_select" disabled class="code-lang-select white-text" style="width:100px"
                title="Select Language">
            </select> -->
            <p style="text-transform: capitalize;" class=" ">java</p>
        </div>
   
        <div class="item">
            <select id="tutorial_editor_HMW5e_font_select" title="Select Editor Font Size" class="code-font-select   ">
            <option value="12px">12px</option><option value="13px">13px</option><option value="14px">14px</option><option value="15px">15px</option><option value="16px">16px</option><option value="17px">17px</option><option value="18px">18px</option></select>
            <!-- <i class="fa fa-text-height code-font-select  "></i> -->
        </div>
       
        
        <div class="item">
            <i id="tutorial_editor_HMW5e_full_screen" class="fa fa-arrows-alt code-fullscreen  " aria-hidden="true" title="FullScreen"></i>
        </div>
         
    </div>
    <div class="col l12 s12 m12 editor ace_editor ace-cobalt ace_dark" id="tutorial_editor_HMW5e" style="font-size: 12px; font-family: monospace;"><textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0;"></textarea><div class="ace_gutter"><div class="ace_layer ace_gutter-layer ace_folding-enabled"></div><div class="ace_gutter-active-line" style="display: none;"></div></div><div class="ace_scroller"><div class="ace_content"><div class="ace_layer ace_print-margin-layer"><div class="ace_print-margin" style="left: 4px; visibility: hidden;"></div></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_text-layer" style="padding: 0px 4px;"></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_cursor-layer ace_hidden-cursors"><div class="ace_cursor"></div></div></div></div><div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 22px;"><div class="ace_scrollbar-inner" style="width: 22px;"></div></div><div class="ace_scrollbar ace_scrollbar-h" style="display: none; height: 22px;"><div class="ace_scrollbar-inner" style="height: 22px;"></div></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;"><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;"></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div></div></div>

   
     <span class="pre-heading  bolder">Output of Above Code</span>
    <pre class="output col l12 s12 m12"></pre>
</div>
</div><p>This implementation takes the help of the Math. pow() function and helps remove the for loop we had to use for the calculation of divisor and multiplier.</p></div>
                                            </li>
                                        <li class=" col l12 s12 m12 ">
                                                <div class="collapsible-header"><i class="  fa fa-plus fa-str-bg1 s1 "></i>Asked in Companies</div>
                                                <div class="collapsible-body">
                                                    <div class=" flex-card" id="companiesList">
                                                    </div>
                                                </div>
                                            </li>
                                        <li class=" col l12 s12 m12  ">
                                            <div class="collapsible-header"><i class="  fa fa-plus fa-str-bg1 s1 "></i>Related Topics</div>
                                            <div class="collapsible-body">
                                                <div class="   flex-card" id="tagList">
                                                </div>
                                            </div>
                                        </li>
                                    </ul>
                                    <br>
                                    <br>
                                        <div class="row card card-light col l12" id="buyNowFreeCourse"><div class="col l4 s4 m4">
    <img class="image  center " height="80px" width="80px" src="./a8_q8_files/doubt_support.svg">
</div>
<div class="col l8 s8 m8">
    <p class="no-margin">Do you need more personalize experience while solving question
        along with doubt support.</p>
    <a class="btn" href="https://www.pepcoding.com/courses" target="_blank">
        <h4 class="bolder ">Buy Now</h4>
    </a>
</div></div>
                                    <br>
                                    <br>
                                    <br>
                                    <br>
                                    <input type="hidden" value="1138" id="quesId">
                                    <input type="hidden" value="20" id="completeProfilePromptThreshold">
                                    <input type="hidden" value="false" id="isPrivate">
                                </div>
                                        <div id="updateProfileModal135086" class="modal small" style="z-index: 1015;">
                                            <div class="modal-content">
                                                <div class="row">
                                                    <div class="row no-margin">
                                                        <h1 class="col l10 s10 m10 center no-margin">Update Your Profile</h1>
                                                        <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion#!" class="col l2 s2 m2 modal-close waves-effect waves-green"> <i class="svg-close svg-header"></i></a>
                                                    </div>
                                                    <div class="row">
                                                        <div class="card">
                                                            <div class="card-content">
                                                                <br>
                                                                <div class="row center">
                                                                    <h3>Your profile is incomplete!</h3>
                                                                    <br>
                                                                    <h3>Please <a href="https://www.pepcoding.com/profile" target="_blank"><u>click here</u></a> to complete your profile
                                                                        to continue submitting
                                                                        questions.</h3>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div></div>
                            
                            
                            
                            <div id="solutionContainer" class="resource-content  row card-content resource-content no-padding" style="display: none;">
                                <div class="col l11 s11 m11  ">
                            
                            
                                    <div class="row col l12 s12 m12 ">
                            
                                        <h1 class=" center">Video Solution </h1>
                            
                                        <iframe src="./a8_q8_files/lt8oCGqYMGg.html" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen="" height="350px" width="100%"></iframe>
                            
                                    </div>
                            
                                </div>
                            
                                <div class="col l11 s11 m11 ">
                                    <div class="row col l12 s12 m12">
                            
                                        <h1 class=" center" style=" ">Code Solution </h1>
                                      
                                        <div class="code-container">
                            
                                                <div class=" selectLang  editorOptions showEditorOptions header  no-margin d-flex  ">
                                                    <div class="item">
                                                      <select id="solutionEditor_lang_select" class="code-lang-select text-upper" title="Select Language"></select>
                                                    </div>
                                                    <div class="item settings">
                                                      <i class="fa fa-gear  modal-trigger" href="#solutionEditor_modalSetting"></i>
                                                     
                                                      <i id="solutionEditor_format_code" class="fa fa-format  format-code" aria-hidden="true" title="Format your code">{ } </i>
                                                      <i id="solutionEditor_reset_code" class="fa fa-refresh  code-refresh" aria-hidden="true" title="Reset your code"></i>
                                                      <i id="solutionEditor_full_screen" class="fa fa-arrows-alt code-fullscreen" aria-hidden="true" title="FullScreen"></i>
                                                    </div>
                                                    
                                                    <div id="solutionEditor_modalSetting" class="modal small" style="z-index: 1017;">
                                                      <div class="modal-content">
                                                        <h4 class="row col l12 s12 center">
                                                          Editor Settings
                                                        </h4>
                                                        <div class="row">
                                                          <h4 class="col l6">
                                                            Font Size
                                                          </h4>
                                                          <select id="solutionEditor_font_select" title="Select Editor Font Size" class="code-font-select col l6"></select>
                                                        </div>
                                                        <div class="row">
                                                          <h4 class="col l6">
                                                            Key Binding
                                                          </h4>
                                                          <select id="solutionEditor_key_binding" title="Select Editor Key Binding" class="key-binding col l6"></select>
                                                        </div>
                                                        <div class="divider"></div>
                                                        <div class="row">
                                                          <h4 class="col l12 center">
                                                            Keyboard Shortcut
                                                          </h4>
                                                        </div>
                                                        <ul class="collection">
                                                          <li class="collection-item list-item">
                                                            <span class="col l6 s6">
                                                              fold
                                                            </span>
                                                            <span class="col l6 s6">
                                                              Alt-L|Ctrl-F1
                                                            </span>
                                                          </li>
                                                          <li class="collection-item list-item">
                                                            <span class="col l6 s6">
                                                              unfold
                                                            </span>
                                                            <span class="col l6 s6">
                                                              Alt-Shift-L|Ctrl-Shift-F1
                                                            </span>
                                                          </li>
                                                          <li class="collection-item list-item">
                                                            <span class="col l6 s6">
                                                              Gotoend
                                                            </span>
                                                            <span class="col l6 s6">
                                                              Ctrl-End
                                                            </span>
                                                          </li>
                                                          <li class="collection-item list-item">
                                                            <span class="col l6 s6">
                                                              Gotostart
                                                            </span>
                                                            <span class="col l6 s6">
                                                              Ctrl-Home
                                                            </span>
                                                          </li>
                                                          <li class="collection-item list-item">
                                                            <span class="col l6 s6">
                                                              Movelinesup
                                                            </span>
                                                            <span class="col l6 s6">
                                                              Alt-Up
                                                            </span>
                                                          </li>
                                                          <li class="collection-item list-item">
                                                            <span class="col l6 s6">
                                                              Movelinesdown
                                                            </span>
                                                            <span class="col l6 s6">
                                                              Alt-Down
                                                            </span>
                                                          </li>
                                                          <li class="collection-item list-item">
                                                            <span class="col l6 s6">
                                                              Undo
                                                            </span>
                                                            <span class="col l6 s6">
                                                              Ctrl-Z
                                                            </span>
                                                          </li>
                                                          <li class="collection-item list-item">
                                                            <span class="col l6 s6">
                                                              Redo
                                                            </span>
                                                            <span class="col l6 s6">
                                                              Ctrl-Shift-Z|Ctrl-Y
                                                            </span>
                                                          </li>
                                                          <li class="collection-item list-item">
                                                            <span class="col l6 s6">
                                                              Replace
                                                            </span>
                                                            <span class="col l6 s6">
                                                              Ctrl-H
                                                            </span>
                                                          </li>
                                                          <li class="collection-item list-item">
                                                            <span class="col l6 s6">
                                                              Togglecomment
                                                            </span>
                                                            <span class="col l6 s6">
                                                              Ctrl-/
                                                            </span>
                                                          </li>
                                                          <li class="collection-item list-item">
                                                            <span class="col l6 s6">
                                                              ToggleBlockComment
                                                            </span>
                                                            <span class="col l6 s6">
                                                              Ctrl-Shift-/
                                                            </span>
                                                          </li>
                                                          <li class="collection-item list-item">
                                                            <span class="col l6 s6">
                                                              Removeline
                                                            </span>
                                                            <span class="col l6 s6">
                                                              Ctrl-D
                                                            </span>
                                                          </li>
                                                        </ul>
                                                      </div>
                                                    </div>                    </div>
                                                 <input type="hidden" value="" id="solutionEditor_sample_code">
                                                <div id="solutionEditor" class="editor " style="  margin-bottom:20px;height:280px;width:100%; ">
                            
                                                
                                        </div>
                                        </div>
                                        
                                    </div>
                            
                            
                                </div>
                            
                            
                            </div>
                            
                            <div id="history" class="card-content resource-content  no-padding" style="display: none;">
                                <div class="row col l12 s12 m12" purpose="questionsHistory">
                                </div>
                            </div>
                            
                            
                            <div id="statsContainer" class="row resource-content " style="display: none;">
                            </div>
                            
                            
                        </div>
                    </div>
                    <div class="gutter gutter-horizontal" style="flex-basis: 10px;"></div><div class="  no-margin no-padding" id="splitEditor" style="flex-basis: calc(50% - 5px);">

                        <div class=" selectLang  editorOptions showEditorOptions header  no-margin d-flex  ">
                            <div class="item">
                              <select id="codeEditor1651_lang_select" class="code-lang-select text-upper" title="Select Language"><option value="cpp">cpp</option><option value="java">java</option><option value="javascript">js</option><option value="python">python</option><option value="ruby">ruby</option></select>
                            </div>
                            <div class="item settings">
                              <i class="fa fa-gear  modal-trigger" href="#codeEditor1651_modalSetting"></i>
                             
                              <i id="codeEditor1651_format_code" class="fa fa-format  format-code" aria-hidden="true" title="Format your code">{ } </i>
                              <i id="codeEditor1651_reset_code" class="fa fa-refresh  code-refresh" aria-hidden="true" title="Reset your code"></i>
                              <i id="codeEditor1651_full_screen" class="fa fa-arrows-alt code-fullscreen" aria-hidden="true" title="FullScreen"></i>
                            </div>
                            <div class="item">
                              <div class="">
                                <i id="codeEditor1651_compile_code" class="fa fa-play code-run btn-compile" title="Run"></i>
                                Run
                              </div>
                            </div>
                            
                            
                            <div id="codeEditor1651_modalSetting" class="modal small" style="z-index: 1019;">
                              <div class="modal-content">
                                <h4 class="row col l12 s12 center">
                                  Editor Settings
                                </h4>
                                <div class="row">
                                  <h4 class="col l6">
                                    Font Size
                                  </h4>
                                  <select id="codeEditor1651_font_select" title="Select Editor Font Size" class="code-font-select col l6"><option value="12px">12px</option><option value="13px">13px</option><option value="14px">14px</option><option value="15px">15px</option><option value="16px">16px</option><option value="17px">17px</option><option value="18px">18px</option></select>
                                </div>
                                <div class="row">
                                  <h4 class="col l6">
                                    Key Binding
                                  </h4>
                                  <select id="codeEditor1651_key_binding" title="Select Editor Key Binding" class="key-binding col l6"><option value="ace/keyboard/sublime">vscode</option><option value="ace/keyboard/emacs">ecmas</option><option value="ace/keyboard/vim">vim</option></select>
                                </div>
                                <div class="divider"></div>
                                <div class="row">
                                  <h4 class="col l12 center">
                                    Keyboard Shortcut
                                  </h4>
                                </div>
                                <ul class="collection">
                                  <li class="collection-item list-item">
                                    <span class="col l6 s6">
                                      fold
                                    </span>
                                    <span class="col l6 s6">
                                      Alt-L|Ctrl-F1
                                    </span>
                                  </li>
                                  <li class="collection-item list-item">
                                    <span class="col l6 s6">
                                      unfold
                                    </span>
                                    <span class="col l6 s6">
                                      Alt-Shift-L|Ctrl-Shift-F1
                                    </span>
                                  </li>
                                  <li class="collection-item list-item">
                                    <span class="col l6 s6">
                                      Gotoend
                                    </span>
                                    <span class="col l6 s6">
                                      Ctrl-End
                                    </span>
                                  </li>
                                  <li class="collection-item list-item">
                                    <span class="col l6 s6">
                                      Gotostart
                                    </span>
                                    <span class="col l6 s6">
                                      Ctrl-Home
                                    </span>
                                  </li>
                                  <li class="collection-item list-item">
                                    <span class="col l6 s6">
                                      Movelinesup
                                    </span>
                                    <span class="col l6 s6">
                                      Alt-Up
                                    </span>
                                  </li>
                                  <li class="collection-item list-item">
                                    <span class="col l6 s6">
                                      Movelinesdown
                                    </span>
                                    <span class="col l6 s6">
                                      Alt-Down
                                    </span>
                                  </li>
                                  <li class="collection-item list-item">
                                    <span class="col l6 s6">
                                      Undo
                                    </span>
                                    <span class="col l6 s6">
                                      Ctrl-Z
                                    </span>
                                  </li>
                                  <li class="collection-item list-item">
                                    <span class="col l6 s6">
                                      Redo
                                    </span>
                                    <span class="col l6 s6">
                                      Ctrl-Shift-Z|Ctrl-Y
                                    </span>
                                  </li>
                                  <li class="collection-item list-item">
                                    <span class="col l6 s6">
                                      Replace
                                    </span>
                                    <span class="col l6 s6">
                                      Ctrl-H
                                    </span>
                                  </li>
                                  <li class="collection-item list-item">
                                    <span class="col l6 s6">
                                      Togglecomment
                                    </span>
                                    <span class="col l6 s6">
                                      Ctrl-/
                                    </span>
                                  </li>
                                  <li class="collection-item list-item">
                                    <span class="col l6 s6">
                                      ToggleBlockComment
                                    </span>
                                    <span class="col l6 s6">
                                      Ctrl-Shift-/
                                    </span>
                                  </li>
                                  <li class="collection-item list-item">
                                    <span class="col l6 s6">
                                      Removeline
                                    </span>
                                    <span class="col l6 s6">
                                      Ctrl-D
                                    </span>
                                  </li>
                                </ul>
                              </div>
                            </div>                        </div>

                        <div id="codeContainer" class="row col l12 s12  card-content row code-container no-padding">
                            <div id="codeEditor1651" class="col l12 s12 m8 editor ace_editor ace-cobalt ace_dark" style="font-size: 12px; font-family: monospace;"><textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; height: 14.4px; width: 6.59775px; left: 97.782px; top: 100.8px;"></textarea><div class="ace_gutter"><div class="ace_layer ace_gutter-layer ace_folding-enabled" style="margin-top: 0px; height: 657.8px; width: 40px;"><div class="ace_gutter-cell " style="height: 14.4px;">1<span class="ace_fold-widget ace_start ace_open" style="height: 14.4px;"></span></div><div class="ace_gutter-cell " style="height: 14.4px;">2</div><div class="ace_gutter-cell " style="height: 14.4px;">3<span class="ace_fold-widget ace_start ace_open" style="height: 14.4px;"></span></div><div class="ace_gutter-cell " style="height: 14.4px;">4</div><div class="ace_gutter-cell " style="height: 14.4px;">5</div><div class="ace_gutter-cell " style="height: 14.4px;">6</div><div class="ace_gutter-cell " style="height: 14.4px;">7</div><div class="ace_gutter-cell " style="height: 14.4px;">8</div></div><div class="ace_gutter-active-line" style="display: none;"></div></div><div class="ace_scroller" style="left: 41px; right: 0px; bottom: 0px;"><div class="ace_content" style="margin-top: 0px; width: 719px; height: 657.8px; margin-left: 0px;"><div class="ace_layer ace_print-margin-layer"><div class="ace_print-margin" style="left: 531.82px; visibility: hidden;"></div></div><div class="ace_layer ace_marker-layer"><div class="ace_active-line" style="height:14.40000057220459px;top:100.80000400543213px;left:0;right:0;"></div><div class="ace_bracket ace_start ace_br15" style="height:14.40000057220459px;width:6.597750244140625px;top:100.80000400543213px;left:36.98875122070312px;"></div></div><div class="ace_layer ace_text-layer" style="padding: 0px 4px;"><div class="ace_line_group" style="height:14.40000057220459px"><div class="ace_line" style="height:14.40000057220459px"><span class="ace_keyword">def</span> <span class="ace_identifier">rotation</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">N</span><span class="ace_paren ace_rparen">)</span>:</div></div><div class="ace_line_group" style="height:14.40000057220459px"><div class="ace_line" style="height:14.40000057220459px">  <span class="ace_identifier">output</span> <span class="ace_keyword ace_operator">=</span> <span class="ace_paren ace_lparen">[</span><span class="ace_paren ace_rparen">]</span></div></div><div class="ace_line_group" style="height:14.40000057220459px"><div class="ace_line" style="height:14.40000057220459px">  <span class="ace_keyword">for</span> <span class="ace_identifier">i</span> <span class="ace_keyword">in</span> <span class="ace_support ace_function">range</span><span class="ace_paren ace_lparen">(</span><span class="ace_support ace_function">len</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">N</span><span class="ace_paren ace_rparen">))</span>: </div></div><div class="ace_line_group" style="height:14.40000057220459px"><div class="ace_line" style="height:14.40000057220459px">   <span class="ace_identifier">output</span>.<span class="ace_identifier">append</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">N</span><span class="ace_paren ace_lparen">[</span><span class="ace_identifier">i</span>:<span class="ace_paren ace_rparen">]</span> <span class="ace_keyword ace_operator">+</span> <span class="ace_identifier">N</span><span class="ace_paren ace_lparen">[</span>:<span class="ace_identifier">i</span><span class="ace_paren ace_rparen">])</span> </div></div><div class="ace_line_group" style="height:14.40000057220459px"><div class="ace_line" style="height:14.40000057220459px">  <span class="ace_keyword">return</span> <span class="ace_identifier">output</span> </div></div><div class="ace_line_group" style="height:14.40000057220459px"><div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">Q</span><span class="ace_keyword ace_operator">=</span><span class="ace_paren ace_lparen">[</span><span class="ace_constant ace_numeric">5</span>,<span class="ace_constant ace_numeric">9</span>,<span class="ace_constant ace_numeric">3</span><span class="ace_paren ace_rparen">]</span> </div></div><div class="ace_line_group" style="height:14.40000057220459px"><div class="ace_line" style="height:14.40000057220459px"><span class="ace_identifier">r</span><span class="ace_keyword ace_operator">=</span><span class="ace_identifier">rotation</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">Q</span><span class="ace_paren ace_rparen">)</span></div></div><div class="ace_line_group" style="height:14.40000057220459px"><div class="ace_line" style="height:14.40000057220459px"><span class="ace_keyword">print</span><span class="ace_paren ace_lparen">(</span><span class="ace_identifier">r</span><span class="ace_paren ace_rparen">)</span></div></div></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_cursor-layer ace_hidden-cursors"><div class="ace_cursor" style="left: 56.782px; top: 100.8px; width: 6.59775px; height: 14.4px;"></div></div></div></div><div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 22px; bottom: 0px;"><div class="ace_scrollbar-inner" style="width: 22px; height: 115.2px;"></div></div><div class="ace_scrollbar ace_scrollbar-h" style="display: none; height: 22px; left: 41px; right: 0px;"><div class="ace_scrollbar-inner" style="height: 22px; width: 719px;"></div></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;"><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;"></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div></div></div>

                            <div class="col l12 no-margin no-padding  editor-footer no-padding ">
                                <ul id="codeEditor1651_collapsible" class="collapsible no-margin colap-code  ">
                                    <li class="no-margin">
                                        <div class="collapsible-header  row no-margin console">
                                            <div class="col l10 s10">
                            
                                                <span>&nbsp; &nbsp; <i class="fa fa-caret-up  downArrowToRotate"></i>
                                                    <span class="hide-on-med-and-down">
                            
                                                    </span> Console
                                                </span>
                                                <span>
                                                    <i class="fa  fa-clock-o"></i>
                                                    <span id="codeEditor1651_compile_time" class="hide-on-med-and-down"> Time</span>
                                                </span>
                                                <span>
                                                    <i class="fa fa-microchip"></i><span class="hide-on-med-and-down" id="codeEditor1651_compile_memory">
                                                        Memory</span>
                                                </span>
                                                <span id="codeEditor1651_compile_status" class="op-heading">
                                                    <i class="fa fa-check-circle"></i>
                            
                                                    <span id="codeEditor1651_message" class="hide-on-med-and-down">Status</span>
                                            </span></div>
                            
                                            <div class="col l2">
                            
                            
                                                <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion#" id="codeEditor1651_submit_code" class="btn btn-submit  center red white-text  bolder " style="height: 35px;line-height:35px">
                                                    &nbsp;Submit</a>
                                            </div>
                                        </div>
                                        <div class="collapsible-body" style="padding: 0px 10px;">
                            
                            
                                            <div class="row  " style="margin-bottom:2px">
                                                <div class="col s12">
                                                    <ul id="codeEditor1651_tab" class="tabs  output-tabs">
                                                        <li id="codeEditor1651_tab_output" class="tab col s3 active">
                                                            <a class="bolder active" href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion#codeEditor1651_output_box">output</a>
                                                        </li>
                                                        <li id="codeEditor1651_tab_input" class="tab col s3"><a class="bolder" id="hello" href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion#codeEditor1651_input_box">input</a>
                                                        </li>
                                                    <li class="indicator" style="left: 0px; right: 0px;"></li></ul>
                                                </div>
                                                <div id="codeEditor1651_output_box" class="col s12 active" style="height: 20vh">
                                                    <pre id="codeEditor1651_compile_actual_output" placeholder="Add your own input here , else programe will run against default test case" class="output no-margin " style="height:100%;overflow-y:scroll" rows="6" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false"></pre>
                            
                                                    <div id="codeEditor1651_submit_actual_output">
                                                    </div>
                                                </div>
                                                <div id="codeEditor1651_input_box" class="col s12" style="height: 100%; line-height: 1rem; width: 98%; display: none;">
                                                    <textarea class="customArea no-margin" id="codeEditor1651_customInput" style="border:none;height: 100% " placeholder="Add your own input here , else programe will run against default test case" rows="6" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false"></textarea>
                                                </div>
                                            </div>
                            
                                        </div>
                                    </li>
                            
                                </ul>
                                <input type="hidden" value="" id="codeEditor1651_compileOnly">
                            </div>


                        <input type="hidden" value="{&quot;cpp&quot;: {&quot;code&quot;: &quot;#include &lt;iostream&gt;\r\n#include&lt;cmath&gt;\r\n\r\nusing namespace std;\r\nint main(){\r\n    int n,k;\r\n    cin&gt;&gt;n&gt;&gt;k;\r\n    \r\n    //write your code here\r\n\r\n}&quot;}, &quot;java&quot;: {&quot;code&quot;: &quot;import java.util.*;\r\n   \r\n   public class Main{\r\n   \r\n   public static void main(String[] args) {\r\n     // write your code here  \r\n    }\r\n   }&quot;}, &quot;ruby&quot;: {&quot;code&quot;: &quot;&quot;}, &quot;python&quot;: {&quot;code&quot;: &quot;&quot;}, &quot;javascript&quot;: {&quot;code&quot;: &quot;&quot;}}" id="codeEditor1651_sample_code">

                        </div>


                    </div>
            </div>
        </div>
    </div>
</div>

   </main>
   <div class="live-editor">
       <div id="editor-support-out" class="sidenav sidenav-editor-window editor-section black right-aligned">
           <div class="row no-margin doubt-header">
               <div class="col l1 s3 m3 row no-margin no-padding ">
                   <a href="https://www.pepcoding.com/index" class="brand-logo">
                       <img class="logo" src="./a8_q8_files/logo.png" alt="logo">
                   </a>
               </div>
               <div class="col l2 s2 m2 no-padding " title="Save" style="display: inline-flex;">
                   <div id="liveEditorId"></div>&nbsp;
               </div>
   
   
               <div class="col l6 s6 m6 no-padding">
   
                   <div class="selectLang d-flex editorOptions  ">
                       <div class="item">
                         <select id="liveEditor_lang_select" class="code-lang-select text-upper" title="Select Language"></select>
                       </div>
                       <div class="item settings">
                         <i class="fa fa-gear  modal-trigger" href="#liveEditor_modalSetting"></i>
                        
                         <i id="liveEditor_format_code" class="fa fa-format  format-code" aria-hidden="true" title="Format your code">{ } </i>
                         <i id="liveEditor_reset_code" class="fa fa-refresh  code-refresh" aria-hidden="true" title="Reset your code"></i>
                         <i id="liveEditor_full_screen" class="fa fa-arrows-alt code-fullscreen" aria-hidden="true" title="FullScreen"></i>
                       </div>
                       <div class="item">
                         <div class="">
                           <i id="liveEditor_compile_code" class="fa fa-play code-run btn-compile" title="Run"></i>
                           Run
                         </div>
                       </div>
                       
                       
                       <div id="liveEditor_modalSetting" class="modal small" style="z-index: 1021;">
                         <div class="modal-content">
                           <h4 class="row col l12 s12 center">
                             Editor Settings
                           </h4>
                           <div class="row">
                             <h4 class="col l6">
                               Font Size
                             </h4>
                             <select id="liveEditor_font_select" title="Select Editor Font Size" class="code-font-select col l6"></select>
                           </div>
                           <div class="row">
                             <h4 class="col l6">
                               Key Binding
                             </h4>
                             <select id="liveEditor_key_binding" title="Select Editor Key Binding" class="key-binding col l6"></select>
                           </div>
                           <div class="divider"></div>
                           <div class="row">
                             <h4 class="col l12 center">
                               Keyboard Shortcut
                             </h4>
                           </div>
                           <ul class="collection">
                             <li class="collection-item list-item">
                               <span class="col l6 s6">
                                 fold
                               </span>
                               <span class="col l6 s6">
                                 Alt-L|Ctrl-F1
                               </span>
                             </li>
                             <li class="collection-item list-item">
                               <span class="col l6 s6">
                                 unfold
                               </span>
                               <span class="col l6 s6">
                                 Alt-Shift-L|Ctrl-Shift-F1
                               </span>
                             </li>
                             <li class="collection-item list-item">
                               <span class="col l6 s6">
                                 Gotoend
                               </span>
                               <span class="col l6 s6">
                                 Ctrl-End
                               </span>
                             </li>
                             <li class="collection-item list-item">
                               <span class="col l6 s6">
                                 Gotostart
                               </span>
                               <span class="col l6 s6">
                                 Ctrl-Home
                               </span>
                             </li>
                             <li class="collection-item list-item">
                               <span class="col l6 s6">
                                 Movelinesup
                               </span>
                               <span class="col l6 s6">
                                 Alt-Up
                               </span>
                             </li>
                             <li class="collection-item list-item">
                               <span class="col l6 s6">
                                 Movelinesdown
                               </span>
                               <span class="col l6 s6">
                                 Alt-Down
                               </span>
                             </li>
                             <li class="collection-item list-item">
                               <span class="col l6 s6">
                                 Undo
                               </span>
                               <span class="col l6 s6">
                                 Ctrl-Z
                               </span>
                             </li>
                             <li class="collection-item list-item">
                               <span class="col l6 s6">
                                 Redo
                               </span>
                               <span class="col l6 s6">
                                 Ctrl-Shift-Z|Ctrl-Y
                               </span>
                             </li>
                             <li class="collection-item list-item">
                               <span class="col l6 s6">
                                 Replace
                               </span>
                               <span class="col l6 s6">
                                 Ctrl-H
                               </span>
                             </li>
                             <li class="collection-item list-item">
                               <span class="col l6 s6">
                                 Togglecomment
                               </span>
                               <span class="col l6 s6">
                                 Ctrl-/
                               </span>
                             </li>
                             <li class="collection-item list-item">
                               <span class="col l6 s6">
                                 ToggleBlockComment
                               </span>
                               <span class="col l6 s6">
                                 Ctrl-Shift-/
                               </span>
                             </li>
                             <li class="collection-item list-item">
                               <span class="col l6 s6">
                                 Removeline
                               </span>
                               <span class="col l6 s6">
                                 Ctrl-D
                               </span>
                             </li>
                           </ul>
                         </div>
                       </div>                </div>
               </div>
               <div class="col l1 s1 m1 right" title="Close Editor">
                   <a class="sidenav-close right " href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion#">
                       <i class="fa fa-times fa-2x " aria-hidden="true"></i>
                   </a>
               </div>
   
           </div>
           <div id="liveCodeContainer" class="card-content row code-container">
               <div id="liveEditor" class="col l12 s12 m12 editor "></div>
   
   
               <div class="col l12 m12 s12 row  no-padding">
                   <div class="col l12 no-margin no-padding  editor-footer no-padding ">
                       <ul id="liveEditor_collapsible" class="collapsible no-margin colap-code  ">
                           <li class="no-margin">
                               <div class="collapsible-header  row no-margin console">
                                   <div class="col l10 s10">
                   
                                       <span>&nbsp; &nbsp; <i class="fa fa-caret-up  downArrowToRotate"></i>
                                           <span class="hide-on-med-and-down">
                   
                                           </span> Console
                                       </span>
                                       <span>
                                           <i class="fa  fa-clock-o"></i>
                                           <span id="liveEditor_compile_time" class="hide-on-med-and-down"> Time</span>
                                       </span>
                                       <span>
                                           <i class="fa fa-microchip"></i><span class="hide-on-med-and-down" id="liveEditor_compile_memory">
                                               Memory</span>
                                       </span>
                                       <span id="liveEditor_compile_status" class="op-heading">
                                           <i class="fa fa-check-circle"></i>
                   
                                           <span id="liveEditor_message" class="hide-on-med-and-down">Status</span>
                                   </span></div>
                   
                                   <div class="col l2">
                   
                                   </div>
                               </div>
                               <div class="collapsible-body" style="padding: 0px 10px;">
                   
                   
                                   <div class="row  " style="margin-bottom:2px">
                                       <div class="col s12">
                                           <ul id="liveEditor_tab" class="tabs  output-tabs">
                                               <li id="liveEditor_tab_output" class="tab col s3 active">
                                                   <a class="active bolder" href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion#liveEditor_output_box">output</a>
                                               </li>
                                               <li id="liveEditor_tab_input" class="tab col s3"><a class="bolder" id="hello" href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion#liveEditor_input_box">input</a>
                                               </li>
                                           </ul>
                                       </div>
                                       <div id="liveEditor_output_box" class="col s12" style="height: 20vh">
                                           <pre id="liveEditor_compile_actual_output" placeholder="Add your own input here , else programe will run against default test case" class="output no-margin " style="height:100%;overflow-y:scroll" rows="6" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false"></pre>
                   
                                           <div id="liveEditor_submit_actual_output">
                                           </div>
                                       </div>
                                       <div id="liveEditor_input_box" class="col s12" style="height: 100%;line-height: 1rem;width: 98%;">
                                           <textarea class="customArea no-margin" id="liveEditor_customInput" style="border:none;height: 100% " placeholder="Add your own input here , else programe will run against default test case" rows="6" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false"></textarea>
                                       </div>
                                   </div>
                   
                               </div>
                           </li>
                   
                       </ul>
                       <input type="hidden" value="true" id="liveEditor_compileOnly">
                   </div>
               </div>
   
               <div id="slide-out-editorslist" style="transform: translateX(105%);width:36vw;top: 0;height: 90%;overflow:auto;" class="sidenav right white no-margin hide">
   
                   <table>
                       <thead>
                           <tr>
                               <th>Id</th>
                               <th>Name</th>
                               <th>
                                   <a href="https://www.pepcoding.com/resources/online-java-foundation/getting-started/rotate-a-number-official/ojquestion#" class="sidenav-close">
                                       <i class="fa fa-times vertical-text-middle" aria-hidden="true"></i>
                                   </a>
                               </th>
                           </tr>
                       </thead>
                       <tbody id="liveEditorNotesList" class="black-text">
                       </tbody>
                   </table>
               </div>
           </div>
       </div>
   </div>   <script src="./a8_q8_files/jquery.min.js.download"></script>
   <script src="./a8_q8_files/materialize.min.js.download"></script>
   <script type="text/javascript" src="./a8_q8_files/ace.js.download"></script>
   <script src="./a8_q8_files/beautify.min.js.download"></script>
   <input type="hidden" name="nadosSlug" value="rotate-a-number">
   <script type="text/javascript" src="./a8_q8_files/common.js.download"></script>
   <script type="text/javascript" src="./a8_q8_files/base.js.download"></script>
   <script type="text/javascript" src="./a8_q8_files/codeEditorWrapper.js.download"></script>
   <script type="text/javascript" src="./a8_q8_files/liveEditor.js.download"></script>

<input type="hidden" name="courseId" value="12">
<input type="hidden" name="lectureId" value="177">
<input type="hidden" name="resourceId" value="1651">
<div id="sidenavOerlay" onclick="openCloseSideNav();" class="sidenav-overlay"></div>
<!--Start of Tawk.to Script-->
<script type="text/javascript">
   function closeBanner() {
      $(".salesBanner").addClass("hide");
   }
   var twakTo = (function () {
      Tawk_API.maximize();
      Tawk_API.showWidget()
   });


   document.addEventListener("DOMContentLoaded", function (event) {
      $('.payCoin').attr('disabled', false);
      $('.payCoin').on('click', function () {
         $('#payCoinForm').submit();
         $(this).attr('disabled', true);
      });


      if (window.history.replaceState) {
         window.history.replaceState(null, null, window.location.href);
      }

      $('.collapsible').collapsible({ inDuration: 100, outDuration: 100 });
      $('.sidenav').sidenav({ edge: 'left' });
      $('.sidenav-doubts-list').sidenav({ edge: 'right', });
      $('.sidenav-doubt-window').sidenav({ edge: 'right', onOpenStart: window.PEP.InitLiveDoubts, onCloseStart: window.PEP.onDoubtWindowClosed });
      $('.sidenav-editor-window').sidenav({ edge: 'right', onOpenStart: window.PEP.InitlizeLiveEditor });
      $('.sidenav-notes-window').sidenav({ edge: 'right', onOpenStart: window.PEP.InitlizeLiveNotes });
      $('.slide-out-admin-chat').sidenav({ edge: 'right', onOpenStart: window.PEP.openDoubtWindow, onCloseStart: window.PEP.closeDoubtWindow });
      var modals = document.querySelectorAll('.modal')
      for (var i = 0; i < modals.length; i++) {
         M.Modal.init(modals[i]);
      }

   });

   function siteThemeSelect(theme) {
      PEP.createCookie('theme', theme, 365, true);
      document.body.classList.remove('theme1');
      document.body.classList.remove('theme2');
      document.body.classList.remove('theme3');
      document.body.classList.remove('theme4');
      document.body.classList.add(theme);
      saveUserPreferences(theme);
   }


   window.addEventListener("pageshow", function (event) {
      var historyTraversal = event.persisted ||
         (typeof window.performance != "undefined" &&
            window.performance.navigation.type === 2);
      if (historyTraversal) {
         // Handle page restore.
         window.location.reload();
      }
   });
</script>
<script type="text/javascript">
   var key = $('#tawkKey').val();

   if (key && key.length > 0) {
      var Tawk_API = {
         onLoad: function () {

            //if ($('#isShowDoubtSupport').val() == 'true') {
            Tawk_API.hideWidget()
            Tawk_API.minimize();
            // }
         },
      };
      var Tawk_LoadStart = new Date();
      (function () {
         var s1 = document.createElement("script"),
            s0 = document.getElementsByTagName("script")[0];
         s1.async = true;
         s1.src = 'https://embed.tawk.to/' + key + '/default';
         s1.charset = 'UTF-8';
         s1.setAttribute('crossorigin', '*');
         s0.parentNode.insertBefore(s1, s0);
      })();
   }


</script>
<!-- Start Alexa Certify Javascript -->
<script type="text/javascript">
   _atrk_opts = { atrk_acct: "pU35u1SZw320l9", domain: "pepcoding.com", dynamic: true };
   (function () { var as = document.createElement('script'); as.type = 'text/javascript'; as.async = true; as.src = "https://certify-js.alexametrics.com/atrk.js"; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(as, s); })();
</script>
<noscript><img src="https://certify.alexametrics.com/atrk.gif?account=pU35u1SZw320l9" style="display:none" height="1"
      width="1" alt="" /></noscript>
<!-- End Alexa Certify Javascript -->
<!--End of Tawk.to Script-->
<script type="text/javascript" src="./a8_q8_files/article.js.download"></script>
        <script type="text/javascript" src="./a8_q8_files/resourceEditor.js.download"></script>
    <script type="text/javascript" src="./a8_q8_files/resources.js.download"></script>
        <script src="./a8_q8_files/platform.js.download" gapi_processed="true"></script>
        <script src="./a8_q8_files/split.min.js.download" integrity="sha512-to2k78YjoNUq8+hnJS8AwFg/nrLRFLdYYalb18SlcsFRXavCOTfBF3lNyplKkLJeB8YjKVTb1FPHGSy9sXfSdg==" crossorigin="anonymous"></script>
        <script type="text/javascript" src="./a8_q8_files/txtEditorWrapper.js.download"></script>
        <script type="text/javascript">
            $(document).ready(function () {
                if (PEP.User.IsSignedIn()) {
                    window.PEP.ShowCompaniesBadges();
                    window.PEP.showTagBadges();
                }
                setTimeout(getCourseMasterDetails, 1000);
                Split(['#splitQuestion', '#splitEditor'], {
                    elementStyle: (dimension, size, gutterSize) => ({
                        'flex-basis': `calc(${size}% - ${gutterSize}px)`,
                    }),
                    gutterStyle: (dimension, gutterSize) => ({
                        'flex-basis': `${gutterSize}px`,
                    }),


                });
            });

            function getCourseMasterDetails() {
                var courseId = PEP.Resources.CourseId();
                $.ajax({
                    url: '/master/course/' + courseId,
                    dataType: 'json',
                    method: 'get',
                    success: function (response) {
                        if (response && response.data) {
                            $("#buyNowFreeCourse").empty().append(response.data);
                        }
                        window.PEP.hideLoader();
                    },
                    error: function (err) {
                        window.PEP.handleException(err);
                    }
                });
            }
        </script>
        <style>
            .flex {
                display: flex;
                flex-direction: row;
            }

            .gutter.gutter-horizontal {
                cursor: ew-resize;
                border-top: 1px solid var(--bg-inv);
                flex-basis: 10px !important;
                opacity: 0.3;
                border-left: 1px solid var(--color2);
                border-right: 1px solid var(--color2);
            }

            .gutter.gutter-horizontal:after {
                content: "\2807";
                position: relative;
                top: 45vh;
                /* font-size: 0.2rem; */
                left: 2px;
            }

            .gutter {
                cursor: ew-resize;
            }
        </style>


<style>
</style>

<div class="sidenav-overlay" style="display: none;"></div><div class="drag-target"></div><div class="sidenav-overlay"></div><div class="drag-target"></div><div class="sidenav-overlay"></div><div class="drag-target right-aligned"></div><iframe name="oauth2relay279071378" id="oauth2relay279071378" src="./a8_q8_files/postmessageRelay.html" tabindex="-1" aria-hidden="true" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe><div style="display: block; visibility: hidden; position: absolute; width: 106px; left: -10000px; top: -10000px;"><table cellpadding="0" cellspacing="0" dir="ltr" style="width:106px;" frame="void" rules="none" class=" gc-bubbleDefault pls-container"><tbody><tr class="gc-reset"><td class="pls-topLeft gc-reset"><img class="gc-reset" style="width:1px !important; height:1px !important; max-width: 1px !important; max-height: 1px !important;" src="./a8_q8_files/border_3.gif"></td><td class="pls-topTail gc-reset"><img class="pls-tailbottom gc-reset" style="width:15px !important; height:9px !important; max-width: 15px !important; max-height: 9px !important;" src="./a8_q8_files/spacer.gif"><img class="pls-spacerbottom gc-reset" style="width:1px !important; height:1px !important; max-width: 1px !important; max-height: 1px !important;" src="./a8_q8_files/spacer.gif"></td><td class="pls-topRight gc-reset"><img class="gc-reset" style="width:1px !important; height:1px !important; max-width: 1px !important; max-height: 1px !important;" src="./a8_q8_files/border_3.gif"></td></tr><tr class="gc-reset"><td class="pls-vertShimLeft gc-reset"><img class="gc-reset" style="width:1px !important; height:4px !important; max-width: 1px !important; max-height: 4px !important;" src="./a8_q8_files/spacer.gif"></td><td class="pls-vertShim gc-reset"><img class="gc-reset" style="width:1px !important; height:4px !important; max-width: 1px !important; max-height: 4px !important;" src="./a8_q8_files/spacer.gif"></td><td class="pls-vertShimRight gc-reset"><img class="pls-dropTR gc-reset" style="width:5px !important; height:4px !important; max-width: 5px !important; max-height: 4px !important;" src="./a8_q8_files/spacer.gif"></td></tr><tr class="gc-reset"><td class="pls-contentLeft gc-reset"><img class="pls-tailright gc-reset" style="width:9px !important; height:15px !important; max-width: 9px !important; max-height: 15px !important;" src="./a8_q8_files/spacer.gif"><img class="pls-spacerright gc-reset" style="width:1px !important; height:1px !important; max-width: 1px !important; max-height: 1px !important;" src="./a8_q8_files/spacer.gif"></td><td class="pls-contentWrap gc-reset"><div class="goog-bubble-content gc-reset"><iframe ng-non-bindable="" frameborder="0" hspace="0" marginheight="0" marginwidth="0" scrolling="no" style="margin:0px;position:absolute;z-index:1;border-style:none;outline:none;width:100px;" tabindex="0" vspace="0" width="100%" id="I0_1673971901058" name="I0_1673971901058" src="./a8_q8_files/subscribe_embed(1).html"></iframe></div></td><td class="pls-dropRight gc-reset"><img class="pls-tailleft gc-reset" style="width:12px !important; height:19px !important; max-width: 12px !important; max-height: 19px !important;" src="./a8_q8_files/spacer.gif"><img class="pls-spacerleft gc-reset" style="width:1px !important; height:1px !important; max-width: 1px !important; max-height: 1px !important;" src="./a8_q8_files/spacer.gif"></td></tr><tr class="gc-reset"><td class="pls-bottomLeft gc-reset"><img class="gc-reset" style="width:1px !important; height:1px !important; max-width: 1px !important; max-height: 1px !important;" src="./a8_q8_files/border_3.gif"></td><td class="gc-reset"><table cellpadding="0" cellspacing="0" style="width:100%" class="gc-reset"><tbody><tr class="gc-reset"><td class="pls-vert gc-reset"><img class="pls-dropBL gc-reset" style="width:4px !important; height:5px !important; max-width: 4px !important; max-height: 5px !important;" src="./a8_q8_files/spacer.gif"></td><td class="pls-dropBottom gc-reset"><img class="pls-tailtop gc-reset" style="width:19px !important; height:13px !important; max-width: 19px !important; max-height: 13px !important;" src="./a8_q8_files/spacer.gif"><img class="pls-spacertop gc-reset" style="width:1px !important; height:1px !important; max-width: 1px !important; max-height: 1px !important;" src="./a8_q8_files/spacer.gif"></td></tr></tbody></table></td><td class="pls-vert gc-reset"><img class="pls-dropBR gc-reset" style="width:5px !important; height:5px !important; max-width: 5px !important; max-height: 5px !important;" src="./a8_q8_files/spacer.gif"></td></tr></tbody></table></div><script async="" charset="UTF-8" src="./a8_q8_files/en.js.download"></script></body></html>
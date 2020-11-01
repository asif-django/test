var vdo_analyticsID = 'UA-113932176-25';
(function(v, d, o, ai) {
    ai = d.createElement('script');
    ai.async = true;
    ai.src = o;
    d.head.appendChild(ai);
})(
    window,
    document,
    'https://www.googletagmanager.com/gtag/js?id=' + vdo_analyticsID
);

function vdo_analytics() {
    window.dataLayer.push(arguments);

}
(function () {
  window.dataLayer = window.dataLayer || [];
  vdo_analytics("js", new Date());
})();
vdo_analytics('event', 'loaded', { send_to: vdo_analyticsID, value:1, event_category: 'vdoaijs' });



try {


function insideSafeFrame() {
  try {
    if(top != self && window.innerWidth > 1) {
      return true;
    }
    if(top.location.href) {
      return false;
    }
  } catch (error) {
    return true;
  }
}



var w_vdo = (insideSafeFrame()) ? window : window.top,
d_vdo = w_vdo.document;
(function (window, document, deps, publisher) {
  var protocol = window.location.protocol;

  window.vdo_ai_ = window.vdo_ai_ || {};
  window.vdo_ai_.cmd = window.vdo_ai_.cmd || [];

  function loadStyleSheet(src, id) {
    var s = document.createElement('link');
    s.id = id;
    s.rel = "stylesheet";
    s.href = protocol + src;
    document.head.appendChild(s);
  }

    function loadPlayerDiv(id,parentId,iframeBurst=false) {
    if (!iframeBurst) {
      if(document.getElementById(id) == null) {
        var s = document.createElement('div');
        s.id = id;
      } else{
        var s = document.getElementById(id);
      }
       if (parentId != '') {
         var parentDiv = document.getElementById(parentId);
         parentDiv.style.display = "block";
         parentDiv.style.width = "100%";
         if (document.getElementById(parentId).parentNode.offsetWidth < 350){
           var margin = (352 - document.getElementById(parentId).parentNode.clientWidth )/2 ;
           parentDiv.style.marginLeft = '-'+margin + 'px';
         }
         parentDiv.appendChild(s);
       } else{
         document.body.appendChild(s);
       }

    } else{

      var parentIframes = top.document.querySelectorAll('iframe');
      for (var i=0; i < parentIframes.length; i++) {
        var el = parentIframes[i];
        if (el.contentWindow === self) {
            // here you can create an expandable ad
            var s = document.createElement('div');
            s.style.zIndex=111;
            s.style.margin = "0 auto";
            s.style.display = "block";
            s.style.position = "relative";
            s.width = 'fit-content';
            s.id = id;
            var googleDiv = el.parentNode;


            if (parentId != '') {
              var parentDiv = document.createElement('div');
              parentDiv.id = parentId;
              parentDiv.style.display = "block";
              parentDiv.style.width = "100%";
              parentDiv.appendChild(s);
              googleDiv.insertBefore(parentDiv, el);
            } else{
              googleDiv.insertBefore(s, el);
            }


            googleDiv.style.width = "auto";
            googleDiv.parentNode.style.width='auto';
            googleDiv.parentNode.style.height='auto';
        }
      }
    }
  }

  var playerLoaded = false;

  var checkTimer = setInterval(function() {
      if(window.initVdo && typeof window.google != 'undefined' && window.google.ima) {
	     callAdframe();
      }
  }, 1000);


  function callAdframe() {
    if(!playerLoaded) {
        playerLoaded = true;
        clearInterval(checkTimer);
        window.vdo_ai_.cmd.push(function() {
          window.initVdo({"desktop":{"show":true,"muted":true,"autoResize":true,"width":640,"height":360,"bottomMargin":10,"topMargin":10,"unitType":"content-floating","leftOrRight":{"position":"right","margin":10},"cancelTimeoutType":{"type":"timeout","eventtype":"readyforpreroll","cancelTimeout":60000},"passback":{"allow":false,"src":"","string":"","timeout":15000},"smallWidth":498,"smallHeight":280,"crossSize":17,"dispose_off":false,"bannerOff":false,"companionOff":false},"mobile":{"dispose_off":false,"show":true,"muted":true,"autoResize":false,"width":333,"height":250,"bottomMargin":10,"topMargin":10,"unitType":"content","leftOrRight":{"position":"right","margin":10},"cancelTimeoutType":{"type":"timeout","eventtype":"readyforpreroll","cancelTimeout":60000},"passback":{"allow":false,"src":"","string":"","timeout":15000},"smallWidth":333,"smallHeight":250,"crossSize":17,"bannerOff":false,"companionOff":false},"bottomMargin":10,"showOnlyFirst":false,"cancelTimeout":10000,"id":"vdo_ai_5409","muted":true,"playsinline":true,"autoplay":true,"preload":true,"video_clickthrough_url":"","content_sources":["videos\/categories\/50MIN.m3u8","videos\/categories\/news2.m3u8","videos\/categories\/News.m3u8","videos\/categories\/sports.m3u8","videos\/categories\/Workout.m3u8","videos\/categories\/entertainment.m3u8"],"pubId":"695","brandLogo":{"img":"","url":""},"coppa":false,"add_on_page_ready":"no","showLogo":true,"parent_div":"v-wallpaperaccess-v1","adbreak_offsets":[0,5,10],"show_on_ad":true,"close_after_first_ad_timer":0,"domain":"wallpaperaccess.com","path":"\/\/a.vdo.ai\/core\/v-wallpaperaccess-v1\/adframe.js","unitId":"_vdo_ads_player_ai_3406","tag_type":"other","hls":false,"media_url":"https:\/\/s.vdo.ai\/","show_on":"ads-ad-started","canAutoplayCheck":true,"bidders":{"0":{"banner":{"prebid":[{"bidder":"appnexus","params":{"placementId":20095073,"floor":0}},{"bidder":"ix","params":{"siteId":"560524","floor":0,"size":[300,250]}},{"bidder":"ix","params":{"siteId":"560524","floor":0,"size":[336,280]}},{"bidder":"openx","params":{"delDomain":"vdoai-d.openx.net","unit":"541218439","floor":"0"}},{"bidder":"pubmatic","params":{"publisherId":"159175","adSlot":"v-wallpaperaccess-v1-mid-10-b-pre-2","floor":"0"}}]},"bids":[{"bidder":"appnexus","params":{"placementId":20095076,"floor":0,"video":{"skippable":true,"playback_method":null}}},{"bidder":"ix","params":{"siteId":"560521","floor":0,"size":[300,250],"video":{"mimes":["video\/mp4","video\/webm","application\/javascript"],"minduration":1,"maxduration":200,"linearity":1,"startdelay":0,"skip":1,"api":[1,2],"protocols":[1,2,3,4,5,6]}}},{"bidder":"openx","params":{"delDomain":"vdoai-d.openx.net","unit":"541218442","floor":"0"}},{"bidder":"pubmatic","params":{"publisherId":"159175","adSlot":"v-wallpaperaccess-v1-mid-10-v-pre-2","video":{"mimes":["video\/mp4","video\/webm","application\/javascript","video\/ogg"],"skippable":true},"floor":"0"}},{"bidder":"rhythmone","params":{"placementId":"214024","floor":0}}]},"5":{"banner":{"prebid":[{"bidder":"appnexus","params":{"placementId":20095074,"floor":0}},{"bidder":"ix","params":{"siteId":"560525","floor":0,"size":[300,250]}},{"bidder":"ix","params":{"siteId":"560525","floor":0,"size":[336,280]}},{"bidder":"openx","params":{"delDomain":"vdoai-d.openx.net","unit":"541218440","floor":"0"}},{"bidder":"pubmatic","params":{"publisherId":"159175","adSlot":"v-wallpaperaccess-v1-mid-10-b-mid1-2","floor":"0"}}]},"bids":[{"bidder":"appnexus","params":{"placementId":20095077,"floor":0,"video":{"skippable":true,"playback_method":null}}},{"bidder":"ix","params":{"siteId":"560522","floor":0,"size":[300,250],"video":{"mimes":["video\/mp4","video\/webm","application\/javascript"],"minduration":1,"maxduration":200,"linearity":1,"startdelay":0,"skip":1,"api":[1,2],"protocols":[1,2,3,4,5,6]}}},{"bidder":"openx","params":{"delDomain":"vdoai-d.openx.net","unit":"541218443","floor":"0"}},{"bidder":"pubmatic","params":{"publisherId":"159175","adSlot":"v-wallpaperaccess-v1-mid-10-v-mid1-2","video":{"mimes":["video\/mp4","video\/webm","application\/javascript","video\/ogg"],"skippable":true},"floor":"0"}},{"bidder":"rhythmone","params":{"placementId":"214024","floor":0}}]},"10":{"banner":{"prebid":[{"bidder":"appnexus","params":{"placementId":20095075,"floor":0}},{"bidder":"ix","params":{"siteId":"560526","floor":0,"size":[300,250]}},{"bidder":"ix","params":{"siteId":"560526","floor":0,"size":[336,280]}},{"bidder":"openx","params":{"delDomain":"vdoai-d.openx.net","unit":"541218441","floor":"0"}},{"bidder":"pubmatic","params":{"publisherId":"159175","adSlot":"v-wallpaperaccess-v1-mid-10-b-mid2-2","floor":"0"}}]},"bids":[{"bidder":"appnexus","params":{"placementId":20095078,"floor":0,"video":{"skippable":true,"playback_method":null}}},{"bidder":"ix","params":{"siteId":"560523","floor":0,"size":[300,250],"video":{"mimes":["video\/mp4","video\/webm","application\/javascript"],"minduration":1,"maxduration":200,"linearity":1,"startdelay":0,"skip":1,"api":[1,2],"protocols":[1,2,3,4,5,6]}}},{"bidder":"openx","params":{"delDomain":"vdoai-d.openx.net","unit":"541218444","floor":"0"}},{"bidder":"pubmatic","params":{"publisherId":"159175","adSlot":"v-wallpaperaccess-v1-mid-10-v-mid2-2","video":{"mimes":["video\/mp4","video\/webm","application\/javascript","video\/ogg"],"skippable":true},"floor":"0"}},{"bidder":"rhythmone","params":{"placementId":"214024","floor":0}}]}},"waterfallTags":{"0":["googleads.g.doubleclick.net\/pagead\/ads?client=ca-video-pub-7094677798399606&slotname=v-wallpaperaccess-v1-mid-7-v-pre-2&ad_type=video&description_url=http%3A%2F%2Fwallpaperaccess.com&max_ad_duration=60000&videoad_start_delay=0&vpmute=1&vpa=1"],"5":["googleads.g.doubleclick.net\/pagead\/ads?client=ca-video-pub-7094677798399606&slotname=v-wallpaperaccess-v1-mid-8-v-mid1-2&ad_type=video&description_url=http%3A%2F%2Fwallpaperaccess.com&max_ad_duration=60000&videoad_start_delay=0&vpmute=1&vpa=1"],"10":["googleads.g.doubleclick.net\/pagead\/ads?client=ca-video-pub-7094677798399606&slotname=v-wallpaperaccess-v1-mid-9-v-mid2-2&ad_type=video&description_url=http%3A%2F%2Fwallpaperaccess.com&max_ad_duration=60000&videoad_start_delay=0&vpmute=1&vpa=1"]},"adx":{"0":["v-wallpaperaccess-v1-mid-7-b-pre-2"],"5":["v-wallpaperaccess-v1-mid-8-b-mid1-2"],"10":["v-wallpaperaccess-v1-mid-9-b-mid2-2"],"15":["b-v-wallpaperaccess-mid-4"],"20":["b-v-wallpaperaccess-mid-5"],"25":["b-v-wallpaperaccess-mid-6"]},"style":"","s2s":false,"overflow_size":false,"handle_url_change":true});
        });

    }
  }

  function loadScriptSync(src, id) {
    return new Promise(function(resolve, reject) {
        
        if(src.indexOf('ima3.js') > 0 && document.querySelector('script[src*="imasdk.googleapis.com/js/sdkloader/ima3.js"]')) {
            resolve();
            return false;
        }
        var s = document.createElement("script");
        s.id = id;
        var existingScript = document.getElementById(id);
        
        s.async = true;
        s.src = protocol + src;
        document.body.appendChild(s);
        s.onload = resolve;
        s.onerror = reject;
    })
  }


  function inIframe(){try{return self!==top}catch(r){return!0}}var iframe_Burst=inIframe() ? insideSafeFrame() ? false : true : false;



  //#region full_dependencies
  if(typeof window.initVdo !== 'function') {  // Check for existing dependencies
          loadPlayerDiv('_vdo_ads_player_ai_3406','v-wallpaperaccess-v1',iframe_Burst);
            Promise.all([
              loadScriptSync(deps + "dependencies_hbv4/vdo.min.js", "_vdo_ads_css_5654_"),
              loadScriptSync("//imasdk.googleapis.com/js/sdkloader/ima3.js", "_vdo_ads_sdk_5654_")
            ]).then(function() {
               callAdframe();
          })
        }
  //#endregion

})(w_vdo, d_vdo, '//a.vdo.ai/core/', 'v-wallpaperaccess-v1');


} catch (e) {


    vdo_analytics('event', 'Err:' + (btoa(e.message).substr(0,10)), { send_to: vdo_analyticsID, value:1, event_category: 'VDOError' });


    var oReq = new XMLHttpRequest();
    oReq.open('get', '//a.vdo.ai/core/logger.php?msg=' + encodeURIComponent(e.stack)+ '&tag=v-wallpaperaccess-v1&code='+btoa(e.message).substr(0,10) + '&url=' + encodeURIComponent(location.href)  + '&func=vdo.ai.js', true);
    oReq.send();
}
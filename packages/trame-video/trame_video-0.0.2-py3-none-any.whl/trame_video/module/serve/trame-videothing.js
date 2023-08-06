(function (global, factory) {
  typeof exports === 'object' && typeof module !== 'undefined' ? factory(exports, require('panzoom'), require('fabric')) :
  typeof define === 'function' && define.amd ? define(['exports', 'panzoom', 'fabric'], factory) :
  (global = global || self, factory(global.videothing = {}, global.panzoom, global.fabric));
}(this, function (exports, panzoom, f2) { 'use strict';

  panzoom = panzoom && panzoom.hasOwnProperty('default') ? panzoom['default'] : panzoom;
  var f2__default = 'default' in f2 ? f2['default'] : f2;

  /**
   * Observable base class.
   */
  class Observable {
    constructor(events = []) {
      this.events = events;
      this.observers = {};
    }

    /**
       * Register event listener with the observable
       * @param {String} eventName event name
       * @param {Function} callback callback function
       */
    $on(eventName, callback) {
      if (this.events.indexOf(eventName) === -1) {
        throw new Error(`${eventName} is not a recognized event`);
      }
      if (eventName in this.observers) {
        this.observers[eventName].push(callback);
      } else {
        this.observers[eventName] = [callback];
      }
    }

    $off(eventName, callback) {
      this.observers[eventName] = this.observers[eventName].filter(c => c !== callback);
    }

    /**
     * Call listeners and wait for any async handlers to resolve before returning.
     * @param {String} eventName event name
     * @param {*} payload callback args
     * @returns {Promise<Array>}
     */
    async $emit(eventName, payload) {
      if (this.events.indexOf(eventName) === -1) {
        throw new Error(`${eventName} is not a recognized event`);
      }
      if (eventName in this.observers) {
        const promises = this.observers[eventName].map(async (callback) => await callback(payload || this));
        return Promise.all(promises);
      }
      return Promise.resolve([]);
    }
  }

  /**
   * AppController brokers user interactions in other areas of a custom app,
   * such as lists and other inputs.  They hold additional UI state only
   * relevant within the context of the app, such as track coloring schemes.
   *
   * AppController should also handle the nuances of integrating videothing's
   * data into your specific UI framework (such as Vue.js).
   * @class
   * @
   * @abstract
   */
  class AppController extends Observable {
    /**
     * @param {Array<String>} events the events this controller should emit.
     */
    constructor(events = []) {
      super(events.concat(['update']));
    }

    /**
     * After a layer has updated its own shape map,
     * it will pass the updated state to appcontroller.
     * AppController should always override layer.
     *
     * Only a Layer should call this method.  It is in the critical path.
     * 
     * @param {ControllerUpdateParams} _params
     */
    updateTracks(_params) {
      throw new Error('unimplemented');
    }
  }

  /**
   * ES6 module and UMD module are structured differently,
   * so shim is necessary for fabric.  Shame on them.
   */
  const fabric = f2.fabric || f2__default;

  /**
   * Binary search in JavaScript.
   * Adapted from https://stackoverflow.com/questions/22697936/binary-search-in-javascript
   * Returns the index of of the element in a sorted array or (-n-1) where n is the
   * insertion point for the new element.
   * The array may contain duplicate elements. If there are more than one equal
   * elements in the array, the returned value can be the index of any one of the equal elements.
   *
   * @param {Array} ar A sorted array
   * @param {*} an element to search for
   * @param {Function} compareFn A comparator function. The function takes two arguments: (a, b) and returns:
   *                                              a negative number  if a is less than b;
   *                                              0 if a is equal to b;
   *                                              a positive number of a is greater than b.
   */
  function binarySearch(ar, el, compareFn) {
    let m = 0;
    let n = ar.length - 1;
    while (m <= n) {
      // eslint-disable-next-line no-bitwise
      const k = (n + m) >> 1;
      const cmp = compareFn(el, ar[k]);
      if (cmp > 0) {
        m = k + 1;
      } else if (cmp < 0) {
        n = k - 1;
      } else {
        return k;
      }
    }
    return -m - 1;
  }

  /**
   * Insert mutates arr.  Not to be used on reactive arrays.
   * @param {Array} arr array
   * @param {*} newval value to add
   * @param {String} key the key the array is sorted by
   */
  function insert(arr, newval, key = 'key') {
    const position = binarySearch(arr, newval, (a, b) => a[key] - b[key]);
    if (position >= 0) {
      // item at newval poisition already exists.
      // eslint-disable-next-line no-param-reassign
      arr[position] = newval;
    } else {
      arr.splice((position * -1) - 1, 0, newval);
    }
  }

  /**
   * Remove mutates arr;
   * @param {Array} arr array
   * @param {*} val value to remove
   * @param {String} key the key the array is sorted by
   */
  function remove(arr, val, key = 'key') {
    const position = binarySearch(arr, val, (a, b) => a[key] - b[key]);
    if (position > 0) {
      arr.splice(position, 1);
    }
  }

  /**
   * FindRange returns elements in the array falling within start, end,
   * including the last element before start and the first after end.
   * @param {Array} arr sorted array
   * @param {Number} start start
   * @param {Number} end end
   * @param {String} key the key the array is sorted by
   */
  function findRange(arr, start, end, key = 'key') {
    if (arr.length === 0) {
      return [];
    } if (start > end) {
      return [];
    }
    let starti = binarySearch(arr, { [key]: start }, (a, b) => a[key] - b[key]);

    // value not in list, binarySearch returned insert position
    if (starti < 0) {
      starti = Math.abs((starti + 1) * -1); // Needed because `-0` is a thing in JS.
    }
    if (starti === 0 && end < arr[0][key]) {
      return []; // start < arr[0], end < arr[0]
    }
    if (starti === arr.length - 1 && start > arr[arr.length - 1][key]) {
      return [];
    }
    let endi = starti + 1;
    while (arr[endi] && (arr[endi][key] <= end)) {
      endi += 1;
    }
    if (starti > 0 && arr[starti][key] > start) {
      starti -= 1;
    }
    if (arr[endi - 1][key] < end) {
      endi += 1;
    }
    return arr.slice(starti, endi); // Include end AND one after the end
  }

  var listutils = /*#__PURE__*/Object.freeze({
    binarySearch: binarySearch,
    insert: insert,
    remove: remove,
    findRange: findRange
  });

  /**
   * Get URL query string parameters as map from full url string.
   * Adapted from https://css-tricks.com/snippets/javascript/get-url-variables/
   * @param  {String} url url string
   * @returns {Object}    parameters as map
   */
  function getParams(url) {
    const params = {};
    const parser = document.createElement('a');
    parser.href = url;
    const query = parser.search.substring(1);
    const vars = query.split('&');
    for (let i = 0; i < vars.length; i += 1) {
      const pair = vars[i].split('=');
      params[pair[0]] = decodeURIComponent(pair[1]);
    }
    return params;
  }

  /**
   * Clamp val between min, max
   * @param {Number} v value to clamp
   * @param {Number} min
   * @param {Number} max
   */
  function valBetween(v, min, max) {
    return (Math.min(max, Math.max(min, v)));
  }

  /**
   * Scale array of numbers
   * @param {Array<Number>} box
   * @param {Number} scale
   */
  function scaleBox(box, scale) {
    return box.map((value) => value * scale);
  }

  /**
   * Autonormalize an array
   */
  function autonormalize(arr, {
    domain = [0, 100],
    range = [0, 1],
  } = {}) {
    let dmin = domain[0];
    let dmax = domain[1];
    if (typeof dmin !== 'number') {
      dmin = Math.min(...arr);
    }
    if (typeof dmax !== 'number') {
      dmax = Math.max(...arr);
    }
    const rmin = range[0];
    const rmax = range[1];
    return arr.map((e) => (((e - dmin) / (dmax - dmin)) * (rmax - rmin)) + rmin);
  }

  var index = /*#__PURE__*/Object.freeze({
    autonormalize: autonormalize,
    getParams: getParams,
    listutils: listutils,
    scaleBox: scaleBox,
    valBetween: valBetween
  });

  /**
   * @param {Array<Detection>} detections
   */
  function sortDetections(detections) {
    return detections.sort((da, db) => da.frame - db.frame);
  }

  class Track extends Observable {
    constructor(key, {
      meta = {},
      detections = [],
      begin = Infinity,
      end = 0,
    }) {
      super(['update']);

      /**
       * @name Track#key
       * @type {String}
       */
      this.key = key;

      /**
       * @name Track#meta
       * @type {Object}
       * @default {}
       */
      this.meta = meta;

      /**
       * @name Track#detections
       * @type {Array<Detection>}
       * @default []
       */
      this.detections = sortDetections(detections);

      /**
       * @name Track#begin
       * @type {Frame}
       * @default 0
       */
      this.begin = begin;

      /**
       * @name Track#end
       * @type {Frame}
       * @default 0
       */
      this.end = end;

      /**
       * @name Track#revision
       * @type {Number}
       * @default 0
       */
      this.revision = 0;
    }

    /**
     * @param {String} value
     */
    setKey(value) {
      this.key = value;
      this.update();
    }

    /**
     * @param {Frame} value
     */
    setBegin(value) {
      this.begin = value;
      this.update();
    }

    /**
     * @param {Frame} value
     */
    setEnd(value) {
      this.end = value;
      this.update();
    }

    /**
     * @param {String} key
     * @param {*} value
     */
    setMeta(key, value) {
      this.meta[key] = value;
      this.update();
    }

    /**
     * @param {String} key
     */
    removeMeta(key) {
      delete this.meta[key];
      this.update();
    }

    /**
     * @param {...Detection} detections
     */
    setDetections(...detections) {
      detections.forEach(({ frame, box, image = null, meta = {}}) => {
        if (frame < this.begin) this.begin = frame;
        else if (frame > this.end) this.end = frame;
        insert(this.detections, {
          frame, box, image, meta,
        }, 'frame');
      });
      this.update();
    }

    /**
     * @param {Detection} detection
     */
    removeDetection(detection) {
      remove(this.detections, detection, 'frame');
      this.update();
    }

    /**
     * Get range of detections with final detection interpolated
     * @param {Frame} start
     * @param {Frame} end
     * @return {Array<Detection>}
     */
    getRange(start, end) {
      const r = findRange(this.detections, start, end, 'frame');
      if (r.length >= 2) {
        const endFrame = Track.interpolateFrames(end, r[r.length - 2], r[r.length - 1]);
        r[r.length - 1] = endFrame;
        return r;
      } if (r.length === 1) {
        return r;
      }
      return [];
    }

    update() {
      this.revision += 1;
      this.$emit('update', this);
    }

    /**
     * Returns the linear interpolation between d0 and d1 at currentFrame
     * @param {Frame} currentFrame frame between d0 and d1
     * @param {Detection} d0 starting detection
     * @param {Detection} d1 ending detection
     * @returns {Detection}
     */
    static interpolateFrames(currentFrame, d0, d1) {
      const len = d1.frame - d0.frame;
      // a + b = 1; interpolate from a to b
      const b = Math.abs((currentFrame - d0.frame) / len);
      const a = 1 - b;
      let interpolated = true;
      if (b === 0 || a === 0) {
        interpolated = false; // actually this is a keyframe
      }
      let box;
      if (d0.box) {
        box = d0.box.map((_, i) => ((d0.box[i] * a) + (d1.box[i] * b)));
      }
      const meta = { ...d0.meta, interpolated };
      const frame = Math.round((d0.frame * a) + (d1.frame * b));
      return {
        ...d0,
        meta,
        frame,
        box,
      };
    }
  }

  function between(x, min, max) {
    return x >= min && x <= max;
  }

  /**
   * TrackStore holds and retrieves tracks for a Layer.
   */
  class TrackStore extends Observable {
    constructor() {
      super(['update', 'add', 'remove', 'track-update']);

      /**
       * @name TrackStore#tracks
       * @type {Array<Track>}
       * @default []
       * @private
       */
      this.tracks = []; // reference for fast iteration

      /**
       * @name TrackStore#trackMap
       * @type {Map<String, Track>}
       * @default {}
       * @private
       */
      this.trackMap = {}; // reference for fast lookup
    }

    /**
     * getDetections should ONLY be called by a Layer.
     * getDetections is in the critical path.
     * @param {Frame} startframe
     * @param {Frame} endframe
     * @returns {TrackStoreUpdateParams}
     */
    getDetections(startframe, endframe) {
      let start = Math.round(startframe);
      let end = Math.round(endframe || startframe); // include the last frame
      if (endframe < startframe) {
        const tmp = end;
        end = start;
        start = tmp;
      }
      if (start < 0 || end < 0) {
        return [];
      }
      return this.tracks
        .filter((track) =>
          between(start, track.begin, track.end)
          || between(end, track.begin, track.end)
          || between(track.begin, start, end))
        .map((track) => {
          const detections = track.getRange(start, end);
          const { key, meta, begin, end: _end } = track;
          return { track: { key, meta, begin, end: _end }, detections };
        });
    }

    /**
     * Get track reference by ID
     * @param {string} key track key
     * @returns {Track}
     */
    getTrack(key) {
      return this.trackMap[key];
    }

    /**
     * get the track that ends last
     */
    getLastTrack() {
      let lastTrack = null;
      this.tracks.forEach(t => {
        if (!lastTrack || lastTrack.end < t.end) {
          lastTrack = t;
        }
      });
      return lastTrack;
    }

    /**
     * Add tracks to the trackstore
     * @param  {...Track} tracks 1 or more tracks to add
     */
    add(...tracks) {
      this.tracks.push(...tracks);
      const update = (args) => this.onTrackUpdate(args);
      tracks.forEach((t) => {
        if (t.key in this.trackMap) {
          this.trackMap[t.key].$off('update', update);
        }
        t.$on('update', update);
        this.trackMap[t.key] = t;
      });
      this.$emit('add', tracks);
      this.$emit('update', this);
    }

    /**
     * Remove tracks
     * @public
     * @param {...String} keys 1 or more keys to remove
     */
    remove(...keys) {
      this.tracks = this.tracks.filter((t) => keys.indexOf(t.key) >= 0);
      keys.forEach((k) => delete this.trackMap[k]);
      this.$emit('remove', keys);
      this.$emit('update', this);
    }

    /**
     * Reset trackstore
     */
    reset() {
      const keys = Object.keys(this.trackMap);
      this.tracks = [];
      this.trackMap = {};
      this.$emit('remove', keys);
      this.$emit('update', this);
    }

    onTrackUpdate(args) {
      this.$emit('track-update', args);
    }
  }

  class WebsocketTrackStore extends TrackStore {
    /**
     * @param {string} server URI
     * @param {string} tracksha1 track to request
     */
    constructor(server, tracksha1) {
      super();
      this.server = server;
      this.tracksha1 = tracksha1;
      this.loadedToFrame = 0;
      this.ws = new WebSocket(server);
      this.ws.onmessage = (m) => this.handle(m);
      this.ws.onopen = () => this.ws.send(JSON.stringify({
        tracksha1: this.tracksha1,
      }));
    }

    /**
     * close the connection
     */
    disconnect() {
      this.ws.close();
      this.$emit('update', this);
    }

    /**
     * @param {string} message message from server
     */
    handle(message) {
      const msg = JSON.parse(message.data);
      const { frame, pairs } = msg;
      this.loadedToFrame = frame;
      pairs.forEach(p => {
        const { track, detections } = p;
        const { key, meta, begin } = track;
        const existing = this.getTrack(key);
        if (existing) {
          // if currentFrame is the last frame of a track, detections.length === 1
          const currentFrame = detections[1] || detections[0];
          existing.setDetections(...detections);
          existing.setEnd(currentFrame.frame);
        } else {
          this.add(new Track(key, {
            detections,
            meta,
            begin,
            end: detections[detections.length - 1].frame,
          }));
        }
      });
      this.$emit('update', this);
    }
  }



  var index$1 = /*#__PURE__*/Object.freeze({
    Track: Track,
    TrackStore: TrackStore,
    WebSocketTrackstore: WebsocketTrackStore
  });

  /**
   * @module videothing/Source
   */

  const FlickConstant = 705600000;
  /**
   * Source describes the interface for a clock source.
   * It will normally be static video, but it could also be
   * - a slideshow with hardcoded frame numbers for the slides
   * - an MPEG:DASH live video stream
   * - an audio element, for use with only the track visualization elemnts.
   * - a single image
   *
   * Source should emit events
   * - "update" whenever it is externally updated, such as the source media changing.
   * - "tick" when the clock advances
   * - "ready" when the clock is ready to be run.
   * 
   * @augments Observable
   * @abstract
   */
  class Source extends Observable {
    /**
     * @param {HTMLElement} el
     * @param {Array<string>} events
     */
    constructor(el, events) {
      super(events.concat(['ready', 'update', 'tick', 'resize']));
      this.ready = false;
      // default before real values are known
      this.width = 1920;
      this.height = 1080;
      this.frametime = 0;
      this.flicks = 0;
      this.el = el;
      this.el.setAttribute('style', 'width: 100%');
      const ro = new ResizeObserver(() => this.$emit('resize', this));
      ro.observe(el);
    }

    /**
     * @name Source#playing
     * @type {boolean}
     */
    get playing() { throw new Error('unimplemented'); }

    set playing(val) { throw new Error('unimplemented'); }

    /**
     * @name Source#offset
     * @type {tdm.Frame}
     */
    get offset() { throw new Error('unimplemented'); }

    set offset(val) { throw new Error('unimplemented'); }

    /**
     * Different from duration.  Length is the intrensic length of a source media element.
     * 
     * @name Source#length
     * @type {tdm.Frame}
     */
    get length() { throw new Error('unimplemented'); }

    set length(val) { throw new Error('unimplemented'); }

    /**
     * Duration is the window of frames we are interested in.
     * Normally length == duration
     *
     * @name Source#duration
     * @type {tdm.Frame}
     */
    get duration() { throw new Error('unimplemented'); }

    set duration(val) { throw new Error('unimplemented'); }

    /**
     * @name Source#framerate in frames per second
     * @type {number}
     */
    get framerate() { throw new Error('unimplemented'); }

    set framerate(val) { throw new Error('unimplemented'); }

    /**
     * @param {tdm.Frame} frame
     */
    setTime(frame) {
      throw new Error('unimplemented');
    }

    /**
     * The ratio of element width to the media element's intrinsic width
     * 
     * @returns {number}
     */
    getScale() {
      return this.el.offsetWidth / this.width;
    }

    /**
     * @returns {boolean}
     */
    isReady() {
      return this.ready;
    }
  }

  /**
   * @module videothing/Container
   */

  const DefaultFabricOptions = {
    selection: false, // don't enable drag to group select
    renderOnAddRemove: false, // wait for renderAll() to redraw
    uniScaleTransform: true, // When true, objects can be transformed by one side (unproportionally)
  };
  const DefaultPanzoomOptions = {
    smoothScroll: false,
  };

  /**
   * Options for the Container constuctor
   * @typedef {Object} ContainerOptions
   * @property {Boolean} debug enable debug mode
   * @property {Boolean} handleScale whether to handle scaling in the container or the layer
   * @property {Object} fabricOptions options for fabric constructor
   * @property {Object} panzoomOptions options for panzoom constructor
   */

  /**
   * Container class sets up Fabric.js canvas and event handlers.
   * Handles injecting the video regin into the DOM.
   * @class
   * @alias videothing.Container
   * @extends videothing.Observable
   */
  class Container extends Observable {
    /**
     * @param {Source} source
     * @param {ContainerOptions} options
     */
    constructor(source, root, {
      debug = false,
      handleScale = true, // Whether to let the container or the layer handle scaling.
      clickable = true, // Whether or not to pass pointer events onto the video
      fabricOptions = DefaultFabricOptions,
      panzoomOptions = DefaultPanzoomOptions,
    } = {}) {
      if (!source || !root) {
        throw new Error('"source" and "root" are required');
      }
      super(['prerender', 'postrender']);
      this.debug = debug;
      this.root = null;
      this.pz = null;
      this.fabricCanvas = null;
      this.source = source;
      this.scale = 1;
      this.handleScale = handleScale;
      this.panzoomOptions = panzoomOptions;
      this.fabricOptions = fabricOptions;
      this.clickable = clickable;
      this.setRoot(root);
      this.source.$on('update', () => this.render());
      this.source.$on('tick', () => this.render());
      this.source.$on('ready', () => this.setupCanvas());
      this.source.$on('resize', () => this.setupCanvas());
    }

    /**
     * Set the root element
     * @param {HTMLElement} root
     */
    setRoot(root) {
      if (this.root) {
        while (this.root.firstChild) {
          this.root.removeChild(root.firstChild);
        }
      }
      let rootElement = root;
      if (typeof rootElement === 'string') {
        rootElement = document.getElementById(rootElement);
      }

      this.root = rootElement;
      while (rootElement.firstChild) {
        rootElement.removeChild(rootElement.firstChild);
      }
      rootElement.style.position = 'relative';
      rootElement.style.overflow = 'hidden';
      rootElement.style.pointerEvents = this.clickable ? 'all' : 'none';

      const canvas = document.createElement('canvas');
      rootElement.appendChild(canvas); // MUST set canvas in page before initializing fabric.

      const fabricCanvas = new fabric.Canvas(canvas, this.fabricOptions);
      fabricCanvas.wrapperEl.setAttribute('style', 'position: absolute; left: 0; top: 0; z-index: 3;');

      const wrapper = document.createElement('div');
      wrapper.setAttribute('style', 'width: 100%; ');
      wrapper.appendChild(this.source.el);
      rootElement.appendChild(wrapper);

      this.pz = panzoom(wrapper, this.panzoomOptions);
      this.pz.on('pan', (e) => this.pzTransform(e));
      this.pz.on('zoom', (e) => this.pzTransform(e));
      this.fabricCanvas = fabricCanvas;
      this.setupCanvas();
    }

    /**
     * Handler for 'pan' and 'zoom' events from panzoom.
     * Repositions the canvas viewportTransform.
     */
    pzTransform() {
      const sourceScale = this.source.getScale();
      const { x, y, scale: pzScale } = this.pz.getTransform();
      const scale = sourceScale * pzScale;
      // if (this.handleScale) {
        this.fabricCanvas.setZoom(scale);
      // }
      this.scale = scale;
      this.fabricCanvas.absolutePan({
        // invert the panzoom transforms
        x: -1 * x,
        y: -1 * y,
      });
      this.render();
    }

    /**
     * Turn panzoom on and off
     * @param {Boolean} panzoom
     */
    pzToggle(enable = true) {
      if (enable) {
        this.pz.resume();
      } else {
        this.pz.pause();
      }
      return this.pz.isPaused();
    }

    /**
     * Set or reset the zoom and pan programatically
     * @param {Number} x top left x
     * @param {Number} y top left y
     * @param {Number} zoom scaling factor
     */
    zoomAbs(x = 0, y = 0, zoom = 1) {
      this.pz.moveTo(x, y);
      this.pz.zoomAbs(x, y, zoom);
    }

    /**
     * Register layer to the container
     * @param {...Layer} layers
     */
    register(...layers) {
      layers.forEach((l) => l.init(this));
      this.render();
    }

    /**
     * Rerender the state of the canvas.
     */
    async render() {
      await this.$emit('prerender', this);
      this.fabricCanvas.renderAll();
      this.$emit('postrender', this);
    }

    /**
     * Set width and height of the canvas when the source changes.
     */
    setupCanvas() {
      this.fabricCanvas.setWidth(this.source.el.offsetWidth);
      this.fabricCanvas.setHeight(this.source.el.offsetHeight);
      this.pzTransform(this.pz);
    }
  }

  /**
   * @module videothing/ImageSource
   */

  /**
   * ImageSource is a simple image onto which can be drawn only a static set of shapes.
   * It will never tick, and its framerate
   */
  class ImageSource extends Source {
    constructor({
      src,
      framerate = -1, // not applicable
      crossorigin = false,
    } = {}) {
      const image = document.createElement('img');
      super(image, []);
      this.image = image;

      this._src = src;
      this.framerate = framerate;
      this.crossorigin = crossorigin;

      image.addEventListener('load', () => this.onLoad());
      image.setAttribute('src', src);
    }
    /**
     * Manipulate the image source
     * 
     * @returns {string} img src
     */
    get src() {
      return this._src;
    }

    set src(value) {
      this.ready = false;
      this._src = value;
      this.image.setAttribute('src', value);
      this.$emit('update', this);
    }

    onLoad() {
      this.width = this.image.naturalWidth;
      this.height = this.image.naturalHeight;
      this.ready = true;
      this.$emit('ready', this);
    }
  }

  /**
   * @module videothing/VideoSource
   */
  /**
   * VideoSource is a clock source based on playing video from
   * an HTML5 native video container.
   * @extends Source
   */
  class VideoSource extends Source {
    constructor({
      src,
      duration = 0, // int frames
      autoplay = true,
      controls = false,
      muted = true, // property ignored if autoplay is true
      framerate = 30,
      loop = false,
      offset = 0, // int frames
      length = 0, // int frames
    } = {}) {
      const video = document.createElement('video');
      super(video, []);
      this.animationId = null;
      this.video = video;

      this._length = length;
      this._src = src;
      this._offset = offset;
      this._duration = duration;
      this._framerate = framerate;
      this._loop = loop;

      // chrome bug requires that these be set with javascript;
      // https://stackoverflow.com/a/51189390/3347791
      if (autoplay) {
        video.muted = true;
        video.autoplay = true;
      } else if (muted) {
        video.muted = true;
      }
      if (controls) {
        video.setAttribute('controls', '');
      }
      video.addEventListener('loadedmetadata', () => this.onLoadedMetadata());
      video.addEventListener('play', () => this.tick(0, false));
      video.setAttribute('src', src);
    }

    /**
     * @returns {Boolean}
     */
    get playing() {
      return !this.video.paused && !this.video.ended;
    }

    set playing(value) {
      if (value) {
        this.video.play();
      } else {
        this.video.pause();
      }
      this.$emit('update', this);
    }

    /**
     * Manipulate the video source
     */
    get src() {
      return this._src;
    }

    set src(value) {
      this.ready = false;
      this._src = value;
      this.video.setAttribute('src', value);
      this.video.load();
      this.$emit('update', this);
    }

    _setTimeInternal(seconds) {
      this.frametime = Math.round(seconds * this.framerate);
      this.flicks = Math.round(seconds * FlickConstant);
    }

    /**
     * Set time on the video.
     * @param {Number} frame
     * @param {Boolean} prevent whether to prevent update event trigger.
     */
    setTime(frame, prevent = false) {
      this.video.currentTime = frame / this.framerate;
      this._setTimeInternal(frame / this.framerate);
      if (!prevent) {
        this.$emit('update', this);
        this.tick();
      }
    }

    get length() {
      return this._length;
    }

    set length(val) {
      this._length = val;
      this.$emit('update', this);
      this.tick();
    }

    get loop() {
      return this._loop;
    }

    set loop(val) {
      this._loop = val;
      this.$emit('update', this);
    }

    get duration() {
      return this._duration;
    }

    set duration(value) {
      this._duration = value;
      this.$emit('update', this);
      this.tick();
    }

    get framerate() {
      return this._framerate;
    }

    set framerate(value) {
      this._framerate = value;
      this._offset = 0;
      this._duration = Math.round(this.video.duration * this.framerate);
      this._length = Math.round(this.video.duration * this.framerate);
      this.$emit('update', this);
      this.tick();
    }

    get offset() {
      return this._offset;
    }

    set offset(value) {
      this._offset = value;
      this.$emit('update', this);
      this.tick();
    }

    onLoadedMetadata() {
      this.width = this.video.videoWidth;
      this.height = this.video.videoHeight;
      if (!this.ready) {
        this.duration = Math.round(this.video.duration * this.framerate);
        this.length = Math.round(this.video.duration * this.framerate);
      }
      this.ready = true;
      this.$emit('ready', this);
    }

    /**
     * The event loop source for external applications.
     * @param {Number} delta time since last call
     * @param {Boolean} prevent whether to forcefully prevent requestAnimationFrame.
     */
    tick(delta, prevent = true) {
      const {
        animationId, offset, duration, frametime,
      } = this;
      if (animationId && !prevent) {
        window.cancelAnimationFrame(animationId);
      }
      const lastframe = frametime;
      const thisFrame = Math.round(this.video.currentTime * this.framerate);
      if (thisFrame < offset) {
        this.setTime(offset, true);
      } else if (!prevent
        && thisFrame > (offset + duration)) {
        if (this._loop) {
          this.setTime(offset, true);
        } else {
          this.video.pause();
          this.setTime(offset + duration, true);
        }
      } else if ((thisFrame !== lastframe) || prevent) {
        this._setTimeInternal(this.video.currentTime);
      }
      if (this.playing && !prevent) {
        this.$emit('tick', this); // Only tick while actively looping.
        this.animationId = window.requestAnimationFrame((d) => this.tick(d, false));
      }
    }
  }

  /**
   * Base layer class
   */
  class Layer {
    /**
     * @param  {Array<AppController>} controllers
     */
    constructor(controllers) {
      /**
       * @name BasicTrackLayer#appcontroller
       * @type {Array<AppController>}
       * @default null
       */
      this.controllers = controllers;
    }

    /**
     * sets up the shapes in this layer and registers them with the container.
     * init should also register any event hooks on the container, such as 'prerender'
     * as well as any event handlers from external sources.
     * @param {Container} container
     */
    init(container) {
      container.$on('prerender', (c) => this.prerender(c));
      if (this.controllers.length) {
        this.controllers.forEach((c) => {
          c.init(container);
          c.$on('update', () => container.render());
        });
      }
    }

    initshape(shape, context) {
      this.controllers.forEach((c) => {
        c.initshape(shape, context);
      });
    }

    /**
     * @param {ControllerUpdateParams} arg
     */
    notifyControllers(args) {
      if (this.controllers.length) {
        this.controllers.forEach((c) => c.updateTracks(args));
      }
    }

    /**
     * CRITICAL PATH Function (executed at 60 Hz)
     * Update the layer based on current time
     * @abstract
     * @param {Container} container
     */
    prerender(container_) {
      throw new Error('unimplemented');
    }
  }

  /**
   * BasicTrackLayer handles positioning rectangles on the canvas based on rectangular tracks.
   * It doesn't do any fancy track history display, coloring, or user interaction.
   * User is responsible for implementing these things in a subclass, a replacement,
   * or in an AppController.
   */
  class BasicTrackLayer extends Layer {
    /**
     * @param {TrackStore} trackstore
     * @param {Array<AppController>} appcontrollers optional
     */
    constructor(trackstore, appcontrollers = []) {
      super(appcontrollers);
      /**
       * @name BasicTrackLayer#trackstore
       * @type {TrackStore}
       */
      this.trackstore = trackstore;

      /**
       * The container.fabricCanvas already holds references to all shapes.
       * Shapemap is needed as a record of which shapes belong to which track.
       * @name BasicTrackLayer#shapemap
       * @type { Map<{trackKey: String, shapes: Array<Object>} >}
       */
      this.shapemap = {};
    }

    /**
     * @param {Container} container
     */
    init(container) {
      super.init(container);
      this.trackstore.$on('update', () => container.render());
    }

    /**
     * Create a new instance of a track rectangle
     * @param {Container} container
     * @param {Track} track
     * @returns {fabric.Rect}
     */
    getNewShape(container, track) {
      const shape = new fabric.Rect({
        stroke: 'red',
        strokeUniform: true,
        strokeWidth: 4,
        fill: 'transparent',
        transparentCorners: false,
        cornerColor: 'lightblue',
        cornerSize: 10,
        noScaleCache: false, // false causes recache on scale
        selectable: false,
      });
      return shape;
    }

    /**
     * Set shape's position.
     * @param {fabric.Rect} shape
     * @param {Array<Number>} box
     * @param {Number} scale
     */
    static updateShape(shape, box) {
      const b = box;
      const left = b[0];
      const top = b[1];
      const width = (b[2] - b[0]);
      const height = (b[3] - b[1]);
      shape.set({
        left, top, width, height,
      });
      shape.setCoords();
    }

    /**
     * @param {Object<{ track: Track, detections: Array<Detection> }>} param0
     * @param {Container} container
     */
    updateTrack({ track, detections }, container) {
      let shapes = this.shapemap[track.key];
      const detection = detections[detections.length - 1];
      const { box } = detection;
      if (!shapes) {
        const shape = this.getNewShape(container, track);
        /* Must add new shapes to the container's canvas */
        container.fabricCanvas.add(shape);
        shapes = [shape];
        this.shapemap[track.key] = shapes;
        this.initshape(shape, { track });
      }
      const shape = shapes[0];
      BasicTrackLayer.updateShape(shape, box);
    }

    /**
     * Drop references to shapes when their tracks are no longer active.
     * @param {Array<String>} activeKeys keys active on the current view
     */
    pruneShapes(activeKeys, container) {
      Object.keys(this.shapemap).forEach((key) => {
        if (activeKeys.indexOf(key) === -1) {
          container.fabricCanvas.remove(...this.shapemap[key]);
          delete this.shapemap[key];
        }
      });
    }

    /**
     * CRITICAL PATH Function (executed at 60 Hz)
     * Update the layer based on current time
     * @param {Container} container
     */
    prerender(container) {
      const { source } = container;
      if (source.isReady()) {
        const frame = source.frametime;
        const pairs = this.trackstore.getDetections(frame);
        pairs.forEach((value, i) => this.updateTrack(value, container, i === 0));
        this.pruneShapes(pairs.map(({ track }) => track.key), container);
        super.notifyControllers({ frame, flick: source.flicks, pairs, shapemap: this.shapemap });
      }
    }
  }

  class OpenfaceLayer extends Layer {
    /**
     *
     * @param {TrackStore} trackstore
     */
    constructor(trackstore, appcontrollers = [], {
      radius = 2,
      getRadius,
    } = {}) {
      super(appcontrollers);
      /**
       * @name OpenfaceLayer#trackstore
       * @type {TrackStore}
       */
      this.trackstore = trackstore;

      /**
       * @name OpenfaceLayer#shapemap
       * @type { Map<{trackKey: String, shapelist: Array<Object>} >}
       */
      this.shapemap = {};

      this.radius = radius;
      this.getRadius = getRadius || (() => this.radius);
    }

    /**
     * @param {Container} container
     */
    init(container) {
      super.init(container);
      this.trackstore.$on('update', () => container.render());
      // this.trackstore.$on('remove', ())
    }

    /**
     * Create a new instance of a track rectangle
     * @returns {fabric.Rect}
     */
    getNewShape(container) {
      const shape = new fabric.Circle({
        stroke: 'red',
        strokeUniform: true,
        strokeWidth: 2,
        transparentCorners: false,
        cornerColor: 'lightblue',
        cornerSize: 10,
        radius: this.radius,
        fill: 'red',
      });
      shape.on({
        modified: () => {
          container.pz.resume();
        },
        deselected: () => {
          container.pz.resume();
        },
        removed: () => {
          container.pz.resume();
        },
        mousedown: () => {
          container.pz.pause();
        },
      });
      return shape;
    }

    /**
     * Set shape's position.
     * @param {fabric.Rect} shape
     * @param {Array<Number>} box
     */
    updateShape(shape, x, y, radiusSize) {
      const radius = radiusSize || this.radius;
      const left = Math.round(x - radius);
      const top = Math.round(y - radius);
      shape.set({ left, top, radius });
      shape.setCoords();
    }

    /**
     *
     * @param {Object<{ track: Track, detections: Array<Detection> }>} param0
     * @param {Container} container
     */
    updateTrack({ track, detections }, container) {
      let shapelist = this.shapemap[track.key];
      const detection = detections[detections.length - 1];
      const { box, frame, meta } = detection;
      const { features } = meta;
      if (!shapelist) {
        const shapes = box.slice(0, box.length / 2).map(() => {
          const s = this.getNewShape(container);
          this.initshape(s, track);
          return s;
        });
        shapes.forEach((s) => container.fabricCanvas.add(s));
        shapelist = shapes;
        this.shapemap[track.key] = shapelist;
      }
      shapelist.forEach((shape, i) => {
        const boxi = i * 2;
        this.updateShape(shape, box[boxi], box[boxi + 1], this.getRadius(frame, features[i]));
      });
    }

    /**
     * Drop references to shapes when their tracks are no longer active.
     *
     * @param {Array<string>} activeKeys keys active on the current view
     * @param {Container} container
     */
    pruneShapes(activeKeys, container) {
      Object.keys(this.shapemap).forEach((key) => {
        if (activeKeys.indexOf(key) === -1) {
          container.fabricCanvas.remove(...this.shapemap[key]);
          delete this.shapemap[key];
        }
      });
    }
    /**
     * update the layer based on container state
     *
     * @param {Container} container
     */
    prerender(container) {
      const { source } = container;
      const ready = source.isReady();
      if (ready) {
        const frame = source.frametime;
        const pairs = this.trackstore.getDetections(frame);
        pairs.forEach((value, i) => this.updateTrack(value, container, i === 0));
        this.pruneShapes(pairs.map(({ track }) => track.key), container);
        super.notifyControllers({ frame, flick: source.flicks, pairs, shapemap: this.shapemap });
      }
    }
  }

  class SourceNotReadyLayer extends Layer {
    constructor({
      text = 'No source',
    } = {}) {
      super([]);
      /**
       * @name SourceNotReadyLayer#text
       * @type {String}
       * @default 'Source not available'
       */
      this.text = text;
    }

    /**
     * sets up the shapes in this layer and registers them with the container.
     * init should also register any event hooks on the container, such as 'prerender'
     *
     * @param {Container} container
     */
    init(container) {
      super.init(container);
      const { fabricCanvas: canvas, source, scale } = container;
      const width = source.width * scale;
      const height = source.height * scale;
      const textSize = Math.round(height / 10);
      this.overlayBG = new fabric.Rect({
        left: 0,
        top: 0,
        width,
        height,
        fill: 'black',
        opacity: 0.85,
        hasControls: false,
        visible: false,
        selectable: false,
      });
      this.overlayText = new fabric.Text(this.text, {
        top: height / 2 - (textSize),
        left: textSize,
        width,
        fontSize: textSize,
        hasControls: false,
        visible: false,
        fill: 'white',
        fontFamily: 'monospace',
        selectable: false,
      });
      canvas.add(this.overlayBG);
      canvas.add(this.overlayText);
    }

    /**
     * update the layer based on container state
     *
     * @param {Container} container
     */
    prerender(container) {
      const { source } = container;
      const ready = source.isReady();
      this.overlayBG.visible = !ready;
      this.overlayText.visible = !ready;
    }
  }



  var index$2 = /*#__PURE__*/Object.freeze({
    BasicTrack: BasicTrackLayer,
    Openface: OpenfaceLayer,
    SourceNotReady: SourceNotReadyLayer
  });

  const CONTRAST_COLORS = [
    '#6A5ACD', // "slateblue",
    '#00c100', // "lime",
    '#d700d7', // "fuchsia",
    '#f1d700', // "yellow",
    '#FF69B4', // "hotpink"
    '#FF0000', // "red",,
    '#0000b8', // "aqua",
  ];

  const SEQUENCE_COLORS = [
    '#543005',
    '#8c510a',
    '#bf812d',
    '#dfc27d',
    '#f6e8c3',
    '#c7eae5',
    '#80cdc1',
    '#35978f',
    '#01665e',
    '#003c30',
  ];

  const DISABLED_COLOR = '#a0a0a0';

  var constants = /*#__PURE__*/Object.freeze({
    CONTRAST_COLORS: CONTRAST_COLORS,
    SEQUENCE_COLORS: SEQUENCE_COLORS,
    DISABLED_COLOR: DISABLED_COLOR
  });

  exports.AppController = AppController;
  exports.Container = Container;
  exports.ImageSource = ImageSource;
  exports.Layers = index$2;
  exports.Source = Source;
  exports.VideoSource = VideoSource;
  exports.constants = constants;
  exports.tdm = index$1;
  exports.utils = index;

  Object.defineProperty(exports, '__esModule', { value: true });

}));

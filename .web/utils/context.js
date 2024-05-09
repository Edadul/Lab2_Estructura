import { createContext, useContext, useMemo, useReducer, useState } from "react"
import { applyDelta, Event, hydrateClientStorage, useEventLoop, refs } from "/utils/state.js"

export const initialState = {"state": {"is_hydrated": false, "router": {"session": {"client_token": "", "client_ip": "", "session_id": ""}, "headers": {"host": "", "origin": "", "upgrade": "", "connection": "", "pragma": "", "cache_control": "", "user_agent": "", "sec_websocket_version": "", "sec_websocket_key": "", "sec_websocket_extensions": "", "accept_encoding": "", "accept_language": ""}, "page": {"host": "", "path": "", "raw_path": "", "full_path": "", "full_raw_path": "", "params": {}}}}, "state.on_load_internal_state": {}, "state.update_vars_internal_state": {}, "state.state_map": {"map": "<div style=\"width:100%;\"><div style=\"position:relative;width:100%;height:0;padding-bottom:60%;\"><span style=\"color:#565656\">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc=\"&lt;!DOCTYPE html&gt;\n&lt;html&gt;\n&lt;head&gt;\n    \n    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;\n    \n        &lt;script&gt;\n            L_NO_TOUCH = false;\n            L_DISABLE_3D = false;\n        &lt;/script&gt;\n    \n    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;\n    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;\n    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js&quot;&gt;&lt;/script&gt;\n    &lt;script src=&quot;https://code.jquery.com/jquery-3.7.1.min.js&quot;&gt;&lt;/script&gt;\n    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js&quot;&gt;&lt;/script&gt;\n    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;\n    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css&quot;/&gt;\n    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css&quot;/&gt;\n    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css&quot;/&gt;\n    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css&quot;/&gt;\n    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;\n    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;\n    \n            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,\n                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;\n            &lt;style&gt;\n                #map_ff41ac1ebee8661993872bdf89b8738d {\n                    position: relative;\n                    width: 100.0%;\n                    height: 100.0%;\n                    left: 0.0%;\n                    top: 0.0%;\n                }\n                .leaflet-container { font-size: 1rem; }\n            &lt;/style&gt;\n        \n&lt;/head&gt;\n&lt;body&gt;\n    \n    \n            &lt;div class=&quot;folium-map&quot; id=&quot;map_ff41ac1ebee8661993872bdf89b8738d&quot; &gt;&lt;/div&gt;\n        \n&lt;/body&gt;\n&lt;script&gt;\n    \n    \n            var map_ff41ac1ebee8661993872bdf89b8738d = L.map(\n                &quot;map_ff41ac1ebee8661993872bdf89b8738d&quot;,\n                {\n                    center: [0.0, 0.0],\n                    crs: L.CRS.EPSG3857,\n                    zoom: 3,\n                    zoomControl: true,\n                    preferCanvas: false,\n                }\n            );\n\n            \n\n        \n    \n            var tile_layer_fc2cbf7a8ef496de0db4f2cffe2c6ebb = L.tileLayer(\n                &quot;https://tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,\n                {&quot;attribution&quot;: &quot;\\u0026copy; \\u003ca href=\\&quot;https://www.openstreetmap.org/copyright\\&quot;\\u003eOpenStreetMap\\u003c/a\\u003e contributors&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 19, &quot;maxZoom&quot;: 19, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}\n            );\n        \n    \n            tile_layer_fc2cbf7a8ef496de0db4f2cffe2c6ebb.addTo(map_ff41ac1ebee8661993872bdf89b8738d);\n        \n&lt;/script&gt;\n&lt;/html&gt;\" style=\"position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;\" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>", "state_callout": false, "state_callout_2": false, "state_callout_3": false}}

export const defaultColorMode = "light"
export const ColorModeContext = createContext(null);
export const UploadFilesContext = createContext(null);
export const DispatchContext = createContext(null);
export const StateContexts = {
  state: createContext(null),
  state__on_load_internal_state: createContext(null),
  state__update_vars_internal_state: createContext(null),
  state__state_map: createContext(null),
}
export const EventLoopContext = createContext(null);
export const clientStorage = {"cookies": {}, "local_storage": {}}

export const state_name = "state"

// Theses events are triggered on initial load and each page navigation.
export const onLoadInternalEvent = () => {
    const internal_events = [];

    // Get tracked cookie and local storage vars to send to the backend.
    const client_storage_vars = hydrateClientStorage(clientStorage);
    // But only send the vars if any are actually set in the browser.
    if (client_storage_vars && Object.keys(client_storage_vars).length !== 0) {
        internal_events.push(
            Event(
                'state.update_vars_internal_state.update_vars_internal',
                {vars: client_storage_vars},
            ),
        );
    }

    // `on_load_internal` triggers the correct on_load event(s) for the current page.
    // If the page does not define any on_load event, this will just set `is_hydrated = true`.
    internal_events.push(Event('state.on_load_internal_state.on_load_internal'));

    return internal_events;
}

// The following events are sent when the websocket connects or reconnects.
export const initialEvents = () => [
    Event('state.hydrate'),
    ...onLoadInternalEvent()
]

export const isDevMode = true

export function UploadFilesProvider({ children }) {
  const [filesById, setFilesById] = useState({})
  refs["__clear_selected_files"] = (id) => setFilesById(filesById => {
    const newFilesById = {...filesById}
    delete newFilesById[id]
    return newFilesById
  })
  return (
    <UploadFilesContext.Provider value={[filesById, setFilesById]}>
      {children}
    </UploadFilesContext.Provider>
  )
}

export function EventLoopProvider({ children }) {
  const dispatch = useContext(DispatchContext)
  const [addEvents, connectErrors] = useEventLoop(
    dispatch,
    initialEvents,
    clientStorage,
  )
  return (
    <EventLoopContext.Provider value={[addEvents, connectErrors]}>
      {children}
    </EventLoopContext.Provider>
  )
}

export function StateProvider({ children }) {
  const [state, dispatch_state] = useReducer(applyDelta, initialState["state"])
  const [state__on_load_internal_state, dispatch_state__on_load_internal_state] = useReducer(applyDelta, initialState["state.on_load_internal_state"])
  const [state__update_vars_internal_state, dispatch_state__update_vars_internal_state] = useReducer(applyDelta, initialState["state.update_vars_internal_state"])
  const [state__state_map, dispatch_state__state_map] = useReducer(applyDelta, initialState["state.state_map"])
  const dispatchers = useMemo(() => {
    return {
      "state": dispatch_state,
      "state.on_load_internal_state": dispatch_state__on_load_internal_state,
      "state.update_vars_internal_state": dispatch_state__update_vars_internal_state,
      "state.state_map": dispatch_state__state_map,
    }
  }, [])

  return (
    <StateContexts.state.Provider value={ state }>
    <StateContexts.state__on_load_internal_state.Provider value={ state__on_load_internal_state }>
    <StateContexts.state__update_vars_internal_state.Provider value={ state__update_vars_internal_state }>
    <StateContexts.state__state_map.Provider value={ state__state_map }>
      <DispatchContext.Provider value={dispatchers}>
        {children}
      </DispatchContext.Provider>
    </StateContexts.state__state_map.Provider>
    </StateContexts.state__update_vars_internal_state.Provider>
    </StateContexts.state__on_load_internal_state.Provider>
    </StateContexts.state.Provider>
  )
}
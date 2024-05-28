/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext } from "react"
import { EventLoopContext, StateContexts } from "/utils/context"
import { Event, getBackendURL, getRefValue, getRefValues, isTrue } from "/utils/state"
import { InfoIcon as LucideInfoIcon, MenuIcon as LucideMenuIcon, WifiOffIcon as LucideWifiOffIcon, XIcon as LucideXIcon } from "lucide-react"
import { keyframes } from "@emotion/react"
import { Box as RadixThemesBox, Button as RadixThemesButton, Callout as RadixThemesCallout, Container as RadixThemesContainer, Dialog as RadixThemesDialog, Flex as RadixThemesFlex, Tabs as RadixThemesTabs, Text as RadixThemesText, TextField as RadixThemesTextField, Theme as RadixThemesTheme } from "@radix-ui/themes"
import env from "/env.json"
import { Root as RadixFormRoot } from "@radix-ui/react-form"
import { Drawer as VaulDrawer } from "vaul"
import "@radix-ui/themes/styles.css"
import theme from "/utils/theme.js"
import NextHead from "next/head"



export function Fragment_6499b51736be44284c15de43340cb16c () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    <Fragment>
  {isTrue(connectErrors.length >= 2) ? (
  <Fragment>
  <RadixThemesDialog.Root css={{"zIndex": 9999}} open={connectErrors.length >= 2}>
  <RadixThemesDialog.Content>
  <RadixThemesDialog.Title>
  {`Connection Error`}
</RadixThemesDialog.Title>
  <RadixThemesText as={`p`}>
  {`Cannot connect to server: `}
  {(connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : ''}
  {`. Check if server is reachable at `}
  {getBackendURL(env.EVENT).href}
</RadixThemesText>
</RadixThemesDialog.Content>
</RadixThemesDialog.Root>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export function Root_d75a273f82829632ede363faebd3865f () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  
    const handleSubmit_32965986460d8ed873fdfaf602d8bc8a = useCallback((ev) => {
        const $form = ev.target
        ev.preventDefault()
        const form_data = {...Object.fromEntries(new FormData($form).entries()), ...{}}

        addEvents([Event("state.state_map.get_code_airport", {form_data:form_data})])

        if (true) {
            $form.reset()
        }
    })
    

  return (
    <RadixFormRoot className={`Root`} css={{"width": "100%"}} onSubmit={handleSubmit_32965986460d8ed873fdfaf602d8bc8a}>
  <RadixThemesFlex css={{"width": "100%"}} direction={`column`} justify={`center`}>
  <RadixThemesTextField.Input css={{"width": "100%", "height": "40px"}} name={`code_input`} placeholder={`Ex: SFO`} required={true}/>
  <RadixThemesButton css={{"width": "100%", "height": "40px", "marginBottom": "15px", "marginTop": "20px"}} type={`submit`}>
  {`Consult`}
</RadixThemesButton>
</RadixThemesFlex>
</RadixFormRoot>
  )
}

export function Fragment_6607534aa8f638118acac90a6d45c99d () {
  const state__state_map = useContext(StateContexts.state__state_map)



  return (
    <Fragment>
  {isTrue(state__state_map.state_callout_2) ? (
  <Fragment>
  <RadixThemesCallout.Root css={{"icon": "info"}}>
  <RadixThemesCallout.Icon>
  <LucideInfoIcon css={{"color": "var(--current-color)"}}/>
</RadixThemesCallout.Icon>
  <RadixThemesCallout.Text>
  {`All or one of the codes were not found.`}
</RadixThemesCallout.Text>
</RadixThemesCallout.Root>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export function Root_f7b6263957477820e0c1a00463462224 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  
    const handleSubmit_dc4580462badd1d08a72a0742bda1f29 = useCallback((ev) => {
        const $form = ev.target
        ev.preventDefault()
        const form_data = {...Object.fromEntries(new FormData($form).entries()), ...{}}

        addEvents([Event("state.state_map.data_cod", {form_data:form_data})])

        if (true) {
            $form.reset()
        }
    })
    

  return (
    <RadixFormRoot className={`Root`} css={{"width": "100%"}} onSubmit={handleSubmit_dc4580462badd1d08a72a0742bda1f29}>
  <RadixThemesFlex css={{"width": "100%"}} direction={`column`} justify={`center`}>
  <RadixThemesFlex css={{"width": "100%"}} justify={`between`} gap={`2`}>
  <RadixThemesFlex direction={`column`}>
  <RadixThemesText as={`p`} size={`1`}>
  {`Place of departure`}
</RadixThemesText>
  <RadixThemesTextField.Input css={{"width": "100%", "height": "40px"}} name={`airport_departure`} placeholder={`Ex: BOG`} required={true}/>
</RadixThemesFlex>
  <RadixThemesFlex direction={`column`}>
  <RadixThemesText as={`p`} size={`1`}>
  {`Place of destination`}
</RadixThemesText>
  <RadixThemesTextField.Input css={{"width": "100%", "height": "40px"}} name={`airport_destination`} placeholder={`Ex: BCN`} required={true}/>
</RadixThemesFlex>
</RadixThemesFlex>
  <RadixThemesButton css={{"width": "100%", "height": "40px", "marginBottom": "15px", "marginTop": "20px"}} type={`submit`}>
  {`Consult`}
</RadixThemesButton>
</RadixThemesFlex>
</RadixFormRoot>
  )
}

export function Fragment_cb5edf864ed730e6ef1545318d0da5a2 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    <Fragment>
  {isTrue(connectErrors.length > 0) ? (
  <Fragment>
  <LucideWifiOffIcon css={{"color": "crimson", "zIndex": 9999, "position": "fixed", "bottom": "30px", "right": "30px", "animation": `${pulse} 1s infinite`}} size={32}/>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export function Div_bf79c007f67caa07440c53aebe09206f () {
  const state__state_map = useContext(StateContexts.state__state_map)



  return (
    <div css={{"width": "100%", "display": "block", "position": "absolute", "left": "0px", "right": "0px", "top": "0px", "bottom": "0px", "overflow": "hidden"}} dangerouslySetInnerHTML={{"__html": state__state_map.map}}/>
  )
}

export function Fragment_faf796e1ddecefde26a87496d29f0cb2 () {
  const state__state_map = useContext(StateContexts.state__state_map)



  return (
    <Fragment>
  {isTrue(state__state_map.state_callout_3) ? (
  <Fragment>
  <RadixThemesCallout.Root css={{"icon": "info"}}>
  <RadixThemesCallout.Icon>
  <LucideInfoIcon css={{"color": "var(--current-color)"}}/>
</RadixThemesCallout.Icon>
  <RadixThemesCallout.Text>
  {`The source and destination could not be the same.`}
</RadixThemesCallout.Text>
</RadixThemesCallout.Root>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

const pulse = keyframes`
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
`


export function Root_0a11fb96d8377430df7674bc8386ba8d () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  
    const handleSubmit_472a6fcc67ba9369dbd17f38cc062023 = useCallback((ev) => {
        const $form = ev.target
        ev.preventDefault()
        const form_data = {...Object.fromEntries(new FormData($form).entries()), ...{}}

        addEvents([Event("state.state_map.search_cordinate", {input:form_data})])

        if (true) {
            $form.reset()
        }
    })
    

  return (
    <RadixFormRoot className={`Root`} css={{"width": "100%"}} onSubmit={handleSubmit_472a6fcc67ba9369dbd17f38cc062023}>
  <RadixThemesFlex css={{"width": "auto"}} justify={`between`}>
  <RadixThemesBox css={{"width": "auto"}}>
  <RadixThemesFlex>
  <RadixThemesTextField.Input css={{"backgroundColor": "#FFF", "padding": "10px", "width": "350px", "height": "40px", "boxShadow": "2px 2px 5px #A9A9A9"}} name={`search_airport`} placeholder={`Buscar: 41.89193, 12.51133`} radius={`full`}/>
</RadixThemesFlex>
</RadixThemesBox>
</RadixThemesFlex>
</RadixFormRoot>
  )
}

export function Fragment_36785ecb30370b3fda16b95439096d9b () {
  const state__state_map = useContext(StateContexts.state__state_map)



  return (
    <Fragment>
  {isTrue(state__state_map.state_callout) ? (
  <Fragment>
  <RadixThemesCallout.Root css={{"icon": "info"}}>
  <RadixThemesCallout.Icon>
  <LucideInfoIcon css={{"color": "var(--current-color)"}}/>
</RadixThemesCallout.Icon>
  <RadixThemesCallout.Text>
  {`Airport's code not found.`}
</RadixThemesCallout.Text>
</RadixThemesCallout.Root>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export default function Component() {

  return (
    <Fragment>
  <Fragment>
  <div css={{"position": "fixed", "width": "100vw", "height": "0"}}>
  <Fragment_cb5edf864ed730e6ef1545318d0da5a2/>
</div>
  <Fragment_6499b51736be44284c15de43340cb16c/>
</Fragment>
  <RadixThemesFlex align={`start`} css={{"margin": "0", "display": "flex", "height": "100vh"}} gap={`2`}>
  <RadixThemesContainer css={{"position": "absoluite", "display": "block", "width": "100%", "height": "100%", "left": "0px", "right": "0px", "top": "0px", "bottom": "0px"}}>
  <Div_bf79c007f67caa07440c53aebe09206f/>
</RadixThemesContainer>
  <RadixThemesBox css={{"position": "absolute", "top": "20px", "left": "100px"}}>
  <Root_0a11fb96d8377430df7674bc8386ba8d/>
</RadixThemesBox>
  <RadixThemesBox css={{"position": "absolute", "padding": "5px", "backgroundColor": "#FFF", "boxShadow": "2px 2px 4px #D1D1D1", "margin": "0", "display": "flex", "flexDirection": "column", "height": "100vh", "weight": "100px"}}>
  <VaulDrawer.Root css={{"top": "auto", "right": "auto", "height": "100vh", "width": "70px", "padding": "2em", "backgroundColor": "#FFF", "boxShadow": "0px 5px, 0px 0px"}} direction={`left`}>
  <VaulDrawer.Trigger asChild={true}>
  <RadixThemesButton css={{"backgroundColor": "#FFF"}}>
  <LucideMenuIcon css={{"color": "rgb(100,100,120)"}}/>
</RadixThemesButton>
</VaulDrawer.Trigger>
  <VaulDrawer.Overlay css={{"position": "fixed", "left": "0", "right": "0", "bottom": "0", "top": "0", "z_index": 50, "background": "rgba(0, 0, 0, 0.5)", "zIndex": "5"}}/>
  <VaulDrawer.Portal>
  <RadixThemesTheme css={{...theme.styles.global[':root'], ...theme.styles.global.body}}>
  <VaulDrawer.Content css={{"left": "0", "right": "auto", "bottom": "0", "top": "auto", "position": "fixed", "z_index": 50, "display": "flex", "height": "100%", "width": "20em", "padding": "20px", "backgroundColor": "#FFF", "boxShadow": "0px 5px, 0px 0px"}}>
  <RadixThemesFlex align={`start`} css={{"width": "100%"}} direction={`column`} gap={`2`}>
  <RadixThemesFlex css={{"alignItems": "start", "padding": "0 0 5px 0", "width": "100%", "borderWidth": "0px 0px 2px 0px"}} justify={`between`}>
  <RadixThemesBox>
  <RadixThemesText as={`p`} size={`5`}>
  {`AIRPORT MAP`}
</RadixThemesText>
</RadixThemesBox>
  <VaulDrawer.Close asChild={true}>
  <RadixThemesBox>
  <RadixThemesButton css={{"backgroundColor": "#FFF"}}>
  <LucideXIcon css={{"color": "rgb(100,100,120)"}} size={30}/>
</RadixThemesButton>
</RadixThemesBox>
</VaulDrawer.Close>
</RadixThemesFlex>
  <RadixThemesFlex css={{"width": "100%"}} justify={`center`}>
  <RadixThemesTabs.Root defaultValue={`tab1`}>
  <RadixThemesFlex css={{"display": "flex", "alignItems": "center", "justifyContent": "center"}}>
  <RadixThemesTabs.List css={{"marginBottom": "30px"}}>
  <RadixThemesTabs.Trigger css={{"margin": "0 25px 0 0"}} value={`tab1`}>
  {`Airport code`}
</RadixThemesTabs.Trigger>
  <RadixThemesTabs.Trigger css={{"margin": "0 0 0 25px"}} value={`tab2`}>
  {`Airport codes`}
</RadixThemesTabs.Trigger>
</RadixThemesTabs.List>
</RadixThemesFlex>
  <RadixThemesFlex css={{"width": "100%"}} direction={`column`}>
  <RadixThemesTabs.Content css={{"width": "100%"}} value={`tab1`}>
  <RadixThemesFlex css={{"width": "100%"}}>
  <RadixThemesText as={`p`} css={{"aling": "center"}} size={`1`}>
  {`Enter a code below`}
</RadixThemesText>
</RadixThemesFlex>
  <Root_d75a273f82829632ede363faebd3865f/>
  <Fragment_36785ecb30370b3fda16b95439096d9b/>
</RadixThemesTabs.Content>
</RadixThemesFlex>
  <RadixThemesFlex css={{"width": "100%"}} direction={`column`}>
  <RadixThemesTabs.Content css={{"width": "100%"}} value={`tab2`}>
  <RadixThemesFlex css={{"width": "100%"}}>
  <Root_f7b6263957477820e0c1a00463462224/>
</RadixThemesFlex>
  <Fragment_6607534aa8f638118acac90a6d45c99d/>
  <Fragment_faf796e1ddecefde26a87496d29f0cb2/>
</RadixThemesTabs.Content>
</RadixThemesFlex>
</RadixThemesTabs.Root>
</RadixThemesFlex>
</RadixThemesFlex>
</VaulDrawer.Content>
</RadixThemesTheme>
</VaulDrawer.Portal>
</VaulDrawer.Root>
</RadixThemesBox>
</RadixThemesFlex>
  <NextHead>
  <title>
  {`Lab2 Estructura | Index`}
</title>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}

import dash_bootstrap_components as dbc

full_variant = {'margin-Top': '16px', 'color': '#FFFFFF', 'font-family': 'Noto Sans', "maxWidth": "400px",
                'fontWeight': '400px', 'font-size': '13px'}


class Tooltip(dbc.Tooltip):
    """A Tooltip component.
    A component for adding tooltips to any element, no callbacks required!

    Simply add the Tooltip to you layout, and give it a target (id of a
    component to which the tooltip should be attached)

    Keyword arguments:

        - children (a list of or a singular dash component, string or number; optional):
            The children of this component.

        - id (string; optional):
            The ID of this component, used to identify dash components in
            callbacks. The ID needs to be unique across all of the components
            in an app.

        - autohide (boolean; default True):
            Optionally hide tooltip when hovering over tooltip content -
            default True.

        - className (string; optional):
            **DEPRECATED** Use `class_name` instead.  Often used with CSS to
            style elements with common properties.

        - class_name (string; optional):
            Often used with CSS to style elements with common properties.

        - delay (dict; default {show: 0, hide: 50}):
            Control the delay of hide and show events.

            `delay` is a dict with keys:

            - hide (number; optional)

            - show (number; optional)

        - fade (boolean; default True):
            If True, a fade animation will be applied when `is_open` is
            toggled. If False the Alert will simply appear and disappear.

        - flip (boolean; default True):
            Whether to flip the direction of the popover if too close to the
            container edge, default True.

        - is_open (boolean; optional):
            Whether the Tooltip is open or not.

        - key (string; optional):
            A unique identifier for the component, used to improve performance
            by React.js while rendering components See
            https://reactjs.org/docs/lists-and-keys.html for more info.

        - loading_state (dict; optional):
            Object that holds the loading state object coming from
            dash-renderer.

            `loading_state` is a dict with keys:

            - component_name (string; optional):
                Holds the name of the component that is loading.

            - is_loading (boolean; optional):
                Determines if the component is loading or not.

            - prop_name (string; optional):
                Holds which property is loading.

        - placement (a value equal to: 'auto', 'auto-start', 'auto-end', 'top', 'top-start', 'top-end', 'right', 'right-start', 'right-end', 'bottom', 'bottom-start', 'bottom-end', 'left', 'left-start', 'left-end'; default 'auto'):
            How to place the tooltip.

        - style (dict; optional):
            Defines CSS styles which will override styles previously set.

        - target (string | dict; optional):
            The id of the element to attach the tooltip to.

        - trigger (string; default 'hover focus'):
            Space separated list of triggers (e.g. \"click hover focus
            legacy\"). These specify ways in which the target component can
            toggle the tooltip. If omitted you must toggle the tooltip
            yourself using callbacks. Options are: - \"click\": toggles the
            popover when the target is clicked. - \"hover\": toggles the
            popover when the target is hovered over with the cursor. -
            \"focus\": toggles the popover when the target receives focus -
            \"legacy\": toggles the popover when the target is clicked, but
            will also dismiss the popover when the user clicks outside of the
            popover.  Default is \"hover focus\"."""

    def __init__(self, children=None, **tooltip_props):
        # Create a shallow copy of component props if it exists, otherwise create an empty dictionary
        tooltip_props = tooltip_props.copy() if tooltip_props else {}
        # Extract the 'style' property if it exists and remove it from component props
        style = tooltip_props.pop('style', None)
        default_style = {}
        # If style is not None, update the default_style dictionary with the contents of the style dictionary
        if style is not None:
            default_style.update(style)
        tooltip_props['style'] = default_style
        # Call the __init__ method of the parent class with the children and component props arguments
        super().__init__(children=children, **tooltip_props)


class FullVariant(Tooltip):
    """
    Class representing the 'full_variant' style.

    Style:
        - margin-Top: 16px
        - color: #FFFFFF
        - font-family: Noto Sans
        - maxWidth: 400px
        - fontWeight: 400px
        - font-size: 13px
    """

    def __init__(self, children=None, **tooltip_props):
        # Create a shallow copy of component props if it exists, otherwise create an empty dictionary
        tooltip_props = tooltip_props.copy() if tooltip_props else {}
        # Extract the 'style' property if it exists and remove it from component props
        style = tooltip_props.pop('style', None)
        default_style = full_variant
        if style is not None:
            default_style.update(style)
        tooltip_props['style'] = default_style
        # Call the __init__ method of the parent class with the children and component props arguments
        super().__init__(children=children, **tooltip_props)

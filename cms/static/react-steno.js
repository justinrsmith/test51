// Provides shortcut methods to React.DOM
// Also allows props object to be omitted.
// Also, possibly not a good idea.

__reactSteno = function(tag){  // Registers `tag` as a new function
    return function (){        // The actual `tag` function
        var args = Array.prototype.slice.call(arguments)
        if (args[0])
        // Test to see if arg 1 is a props object, or if it has been omitted
        // If content is not appearing, these tests need be tweaked
        if (
            typeof args[0] == 'number'  // Arg 1 is an integer
            || args[0].length           // Arg 1 is a string or array
            || args[0].$$typeof         // Arg 1 is a React element
        ) args.unshift({})              // If arg 1 is not props, add a new empty props object
        return React.DOM[tag].apply('', args)
    }
}

// INCOMPLETE list of which tags should become global vars for
// React.createElement(<tag>). If you get 'not defined' when
// trying to call <tag>(), it needs to be added to this list
__reactStenoTags = [
    'div',
    'table',
    'tbody',
    'thead',
    'tr',
    'th',
    'td',
    'p',
    'a',
    'h1',
    'h2',
    'h3',
    'strong',
    'input',
    'button',
    'form',
    'label',
    'select',
    'option',
    'span'
]

// Set the tag functions in global scope
for (var t = __reactStenoTags.length - 1; t >= 0; t--)
    window[__reactStenoTags[t]] = __reactSteno(__reactStenoTags[t])


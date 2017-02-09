request = function(url, opts){
    // XMLHttpRequest wrapper
    // options: {
    //   method: 'POST' || 'PUT' || 'PATCH' || 'DELETE', // default: 'GET'
    //   success: function(request){},
    //   error: function(request){},
    // }
    var noOp = function(){}
    opts = opts || {}
    opts.error = opts.error || noOp
    opts.success = opts.success || noOp
    method = opts.method || 'GET'
    var r = new XMLHttpRequest()
    r.open(method, url)
    r.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
    r.onerror = opts.error // Network error
    r.onload = function(){
        if (r.status > 399) return opts.error(r) // Application error
        opts.success(r)
    }
    /*opts.error = function(r){
        console.log(r.responseText)
    }*/
    r = opts.alterRequest ? opts.alterRequest(r) : r
    r.send(opts.data)
}

getJSON = function(url, opts){
    // Wraps `u.request` with a json-parsing success handler
    opts = opts || {}
    var success = opts.success
    opts.success = function(r){
        return success(JSON.parse(r.responseText))
    }
    return request(url, opts)
}

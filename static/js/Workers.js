console.log("Worker Inintialized")
let _ = undefined

import("/static/js/BRORN_WORKER_.js").then(function(module){
    // _____ = module
    console.log(module._JS_NAME)
    // return (module)
    _ = module
    _.println(" Worker Framework Loaded")
	_.$send({
		action : "/api/v2/set_farmer_chunk_data",
		method : _.POST,
		func : function (e) {
			_.println("DONE WEBWORKING :::")
		}
	})
})
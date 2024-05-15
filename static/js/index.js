
import("./Bootloader.js").then(function(module){
    _____ = module
    // println(module)
    return (module)

})
 // -----------

let loading = {
    show : function (){$ID('SPINNER_LOADER').style.display="block"},
    hide : function (){$ID('SPINNER_LOADER').style.display="none"}
}

// println(" * Loading Index.js")

// function submit_1(form_class){
//     println(" * Submitting")
//     var form_data_arr = {}
//     var form_data = $CLASS(form_class)
//     var fields = []

//     for (var i = 0; i < form_data.length; i++) {
//         if(form_data[i].type=="checkbox"){
//             form_data_arr[form_data[i].id] = form_data[i].checked
//         }
//         else if (form_data[i].type=="file"){
//             form_data_arr[form_data[i].id] = form_data[i].value // TO BE EDITTED
//         }
//         else{
//             form_data_arr[form_data[i].id] = form_data[i].value
//         }
//         fields.push(form_data[i].id)
//         println(form_data[i].id)
//     }
//     // println(form_data_arr)
//     println(fields)
//     submit_to_(form_class,form_data_arr)
// }

// function submit_to_(t_,data_){
//     $send({
//         action : "/api/todbdti",
//         method : POST,
//         data : $DATA({
//             "table" : t_ ,
//             "data":JSON.stringify(data_)}),
//         func : function (res){
//             println(res)
//         },
//         err : function (){
//             alert(" Error in Saving")
//         }
//     })
// }
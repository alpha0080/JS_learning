
var KJJsonInputStyleA = {
    rtl: false,
    showPreview: false,
    showRemove: false,
    showUpload: false,
    showCancel: false,
    showCaption: false,
    browseClass: "btn btn-info",
    browseLabel: "選取檔案",
    allowedFileExtensions: ["json", "JSON"]
};

var KJImageInputStyleA = {
    rtl: false,
    showPreview: false,
    showRemove: false,
    showUpload: false,
    showCancel: false,
    showCaption: false,
    browseClass: "btn btn-success",
    browseLabel: "選取檔案",
    allowedFileExtensions: ["jpg", "png"]
}


$(document).ready(function() {
    $("#inputDataA").show();
    $("#inputDataB").hide();
    $("#inputDataC").hide();
    $("#input_a").click(function() {
        $("#inputDataA").toggle();
    });
    $("#inputB").click(function() {
        $("#inputDataB").toggle();
    });
    $("#inputC").click(function() {
        $("#inputDataC").toggle();
    });
    $("#infoBox").show();
    $("#inputExtA").click(function() {
        $("#infoBox").toggle();
    });
});


//get Bootstrap dropdown value inputADialog_3
$("#databoxA a").click(function(e){
    e.preventDefault(); // cancel the link behaviour
    var selText = $(this).text();
    $("#menuA_blendMode").text(selText);
    console.log(selText);
    PIXI_globalData.inputA.blendMode = selText
});

$("#inputBGA").fileinput(KJImageInputStyleA);


$('#inputBGA').on('fileloaded', function(event, data, previewId, index) {
    $("#showBGA").val("images/" + data.name);
    delete loader.resources["BGA_image"];
    var imageURL = "images/" + data.name
    PIXI_loader("BGA_image", imageURL);
});



//input A----------------------------

$(document).ready(function() {
    $("#optionsRadiosA1").click(function() {
        console.log('still Image');
        PIXI_globalData.inputA.spritesImageMode = 0;
    });
    $("#optionsRadiosA2").click(function() {
        console.log('sequence Images');
        PIXI_globalData.inputA.spritesImageMode = 1;
    });
});




$("#inputJsonA").fileinput(KJJsonInputStyleA); //load motion JsonA

$('#inputJsonA').on('fileloaded', function(event, data, previewId, index) {
    // console.log(event, data, previewId, index,"filepreupload");
    // console.log(event, data, previewId, index, 'fileloaded');
    // console.log(data.name);
    $("#showMotionJsonA").val(data.name);
    delete loader.resources["MotionJsonA"];
    var jsonURL = "json/" + data.name
    PIXI_loader("MotionJsonA", jsonURL);
   // console.log("jsonURL", jsonURL);
   // console.log('loader', resources);
    PIXI_globalData.inputA.motionJson = jsonURL;
    console.log('PIXI_globalData',PIXI_globalData.inputA)
});




$("#inputSpriteJsonA").fileinput(KJJsonInputStyleA); //load spritesImages jsonA

$('#inputSpriteJsonA').on('fileloaded', function(event, data, previewId, index) {

    $("#showSpriteJsonA").val(data.name);
    delete loader.resources["spritesImagesJsonA"];
    delete loader.resources["spritesImagesJsonA_image"];
    var jsonURL = "sprites/" + data.name
    PIXI_loader("spritesImagesJsonA", jsonURL);
    var imgURL = jsonURL.split('.')[0]+".png"

    PIXI_globalData.inputA.spritesJson = jsonURL;
    PIXI_globalData.inputA.spritesImage = imgURL;


    //$("#info").val("");
    //$("#info").append("admin:"+$("#talk").val()+"\n");  

});


$("#stageDescriptJsonA").fileinput(KJJsonInputStyleA); //load spritesImages jsonA

$('#stageDescriptJsonA').on('fileloaded', function(event, data, previewId, index) {

    $("#showStageDescriptJsonA").val(data.name);
    delete loader.resources["stageDescriptJsonA"];
    var jsonURL = "sprites/" + data.name
    PIXI_loader("stageDescriptJsonA", jsonURL);

    PIXI_globalData.inputA.stageDescriptJsonFile = jsonURL;
    PIXI_globalData.inputA.stageDescriptJsonData = "NONE";
   // console.log('PIXI_globalData',PIXI_globalData.inputA)
});

$("#inputJsonB").fileinput(KJJsonInputStyleA);

$('#inputJsonB').on('fileloaded', function(event, data, previewId, index) {
    // console.log(event, data, previewId, index,"filepreupload");
    console.log(event, data, previewId, index, 'fileloaded');
    console.log(data.name);
    $("#showMotionJsonB").val(data.name);
});

$("#inputSpriteJsonB").fileinput(KJJsonInputStyleA);

$("#inputSprtieImageB").fileinput(KJImageInputStyleA);




$("#inputJsonC").fileinput(KJJsonInputStyleA);

$('#inputJsonC').on('fileloaded', function(event, data, previewId, index) {
    // console.log(event, data, previewId, index,"filepreupload");
    console.log(event, data, previewId, index, 'fileloaded');
    console.log(data.name);
    $("#showMotionJsonC").val(data.name);
});

$("#inputSpriteJsonC").fileinput(KJJsonInputStyleA);

$("#inputSprtieImageC").fileinput(KJImageInputStyleA);




function WriteToFile(text) {


    window.location.href = image;

}
var JsonData = ""



function myFunction() {
    console.log(miniApp.screen.width)
};

var openFile = function(event) {
    JsonData = ""
    var input = event.target;

    var reader = new FileReader();
    reader.onload = function() {
        var text = reader.result;
        JsonData += text
        console.log(JsonData.length);
    };
    reader.readAsText(input.files[0]);
    return JsonData
};

function ooo(event) {
    console.log('asdasd')
}
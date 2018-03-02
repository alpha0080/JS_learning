
$(function() {
    var handle = $("#speedSliderA-handle");
    $("#speedSliderA").slider({
        create: function() {
            handle.text($(this).slider("value"));
        },
        value: 1,
        min: 0,
        max: 5,
        step: 0.1,
        slide: function(event, ui) {
            handle.text(ui.value);
            //console.log(ui.value);
            PIXI_globalData.effect_A.adjust.speed = ui.value
        }
    });
});
$(function() {
    var handle = $("#frameSpeedA-handle");
    $("#frameSpeedA").slider({
        create: function() {
            handle.text($(this).slider("value"));
        },
        value: 1,
        min: 0,
        max: 5,
        step: 0.1,
        slide: function(event, ui) {
            handle.text(ui.value);
           // console.log(ui.value);
            PIXI_globalData.effect_A.adjust.frameSpeed = ui.value
        }
    });
});
$(function() {
    var handle = $("#SpritesSizeA-handle");
    $("#SpritesSizeA").slider({
        create: function() {
            handle.text($(this).slider("value"));
        },
        value: 1,
        min: 0,
        max: 10,
        step: 0.1,
        slide: function(event, ui) {
            handle.text(ui.value);
           // console.log(ui.value);
            PIXI_globalData.effect_A.adjust.spritesSize = ui.value
        }
    });
});

$(function() {
    var handle = $("#SpritesSizeRandomA-handle");
    $("#SpritesSizeRandomA").slider({
        create: function() {
            handle.text($(this).slider("value"));
        },
        value: 0,
        min: -10,
        max: 10,
        slide: function(event, ui) {
            handle.text(ui.value);
           // console.log(ui.value);
            PIXI_globalData.effect_A.adjust.spritesSizeRandom = ui.value

        }
    });
});
$(function() {
    var handle = $("#SpritesRotateA-handle");
    $("#SpritesRotateA").slider({
        create: function() {
            handle.text($(this).slider("value"));
        },
        value: 0,
        min: 0,
        max: 360,
        step: 1,
        slide: function(event, ui) {
            handle.text(ui.value);
           // console.log(ui.value);
            PIXI_globalData.effect_A.adjust.spritesRotation = ui.value
        }
    });
});

$(function() {
    var handle = $("#SpritesRotateRandomA-handle");
    $("#SpritesRotateRandomA").slider({
        create: function() {
            handle.text($(this).slider("value"));
        },
        value: 0,
        min: 0,
        max: 360,
        step: 1,
        slide: function(event, ui) {
            handle.text(ui.value);
           // console.log(ui.value);
            PIXI_globalData.effect_A.adjust.spritesRotationRandom = ui.value
        }
    });
});

$(function() {
    var handle = $("#SpritesframeOffsetA-handle");
    $("#SpritesframeOffsetA").slider({
        create: function() {
            handle.text($(this).slider("value"));
        },
        value: 0,
        min: 0,
        max: 20,
        step: 1,
        slide: function(event, ui) {
            handle.text(ui.value);
            PIXI_globalData.effect_A.adjust.spritesFrameOffset = ui.value

        }
    });
});

    $(function() {
    var handle = $("#SpriteTransA-handle");
    $("#SpriteTransA").slider({
        create: function() {
            handle.text($(this).slider("value"));
        },
        value: 1,
        min: 0,
        max: 1,
        step: 0.01,
        slide: function(event, ui) {
            handle.text(ui.value);
            PIXI_globalData.effect_A.adjust.spritesTrans = ui.value

        }
    });
});


$(function() {
    var handle = $("#SpriteBlurA-handle");
    $("#SpriteBlurA").slider({
        create: function() {
            handle.text($(this).slider("value"));
        },
        value: 0,
        min: 0,
        max: 20,
        slide: function(event, ui) {
            handle.text(ui.value);
            PIXI_globalData.effect_A.adjust.spritesBlur = ui.value
        }
    });
});

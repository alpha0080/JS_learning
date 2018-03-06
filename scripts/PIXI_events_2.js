var drawBox = {

    createNew: function () {
        var draw = {};
        draw.testA = "ggg";
        draw.testB = function () {
            for (var i = 0; i < 10; i++) {
                console.log(i)
            }
        };
        draw.rect = function (x, y, w, h) {
            console.log("testC")
            var graphics = new PIXI.Graphics();

            // set a fill and line style
            graphics.beginFill(0xcc9999, 0.7);
            graphics.lineStyle(1, 0xffd900, 1);
            graphics.drawRect(x, y, w, h);

            graphics.endFill();
            graphics.pivot.x = w / 2;
            graphics.pivot.y = h / 2;
            graphics.x = app.renderer.screen.width / 2;
            graphics.y = app.renderer.screen.height / 2;

            return graphics;
        };
        draw.circle = function (x, y, r) {
            var graphics = new PIXI.Graphics();
            graphics.beginFill(0xaa2255, 1);
            graphics.lineStyle(2, 0x000000, 1);
            graphics.drawCircle(x, y, r);
            graphics.endFill();
            graphics.pivot.x = r;
            graphics.pivot.y = r;
            graphics.x = app.renderer.screen.width / 2;
            graphics.y = app.renderer.screen.height / 2;
            return graphics
        };
        draw.cross = function (x, y, length) {
            var graphics = new PIXI.Graphics();
            graphics.beginFill(0xcccccc, 1);
            graphics.lineStyle(3, 0xcc3333, 1);
            graphics.moveTo(x - length, 0);
            graphics.lineTo(x + length, 0);
            graphics.moveTo(0, y - length);
            graphics.lineTo(0, y + length);
            graphics.pivot.x = x;
            graphics.pivot.y = y;
            graphics.x = app.renderer.screen.width / 2;
            graphics.y = app.renderer.screen.height / 2;
            graphics.endFill();
            return graphics

        };
        draw.bbBox = function (container) {
            console.log("width", container.width, container.height)
            var graphics = new PIXI.Graphics();

            // set a fill and line style
            graphics.beginFill(0xcc9999, 0.7);
            graphics.lineStyle(1, 0xffd900, 1);
            graphics.drawRect(0, 0, 300, 300);

            graphics.endFill();
            graphics.pivot.x = container.width / 2;
            graphics.pivot.y = container.height / 2
            graphics.x = app.renderer.screen.width / 2;
            graphics.y = app.renderer.screen.height / 2;
            return graphics
        };
        return draw;
    } //注意格式，後面別加上;
};

function onDragStart(event) {
    // store a reference to the data
    // the reason for this is because of multitouch
    // we want to track the movement of this particular touch
    this.data = event.data;
    this.alpha = 0.5;
    this.dragging = true;
}

function onDragEnd() {
    this.alpha = 1;
    this.dragging = false;
    // set the interaction data to null
    this.data = null;
}

function onDragMove() {
    if (this.dragging) {
        var newPosition = this.data.getLocalPosition(this.parent);
        this.x = newPosition.x;
        this.y = newPosition.y;
    }
};


var objectInfo = {
    createNew: function () {
        var selectedInfo = {};

        selectedInfo.getInfo = function (selectObject) {
            console.log("selectObject", selectObject, selectObject.name);

            var objectData = {
                "name": selectObject.name,
                "w": selectObject.width,
                "h": selectObject.height,
                "x": selectObject.x,
                "y": selectObject.y,
                "px": selectObject.pivot.x,
                "py": selectObject.pivot.y,
                "r": selectObject.rotation,
                "alpha": selectObject.alpha,
                "vis": selectObject.visible,
                "children": selectObject.children,
                "transform": selectObject.transform,
                "parent": selectObject.parent
            };
            console.log(objectData);
        };

        return selectedInfo;
    } //注意格式，後面別加上;
};

function PIXI_loader(id,url){
	
	var loader = PIXI.loader;
	loader.add(id,url)
			.load(setup);
	
	function setup(){
		console.log(loader;)
	}
	return loader
	
	
	
}
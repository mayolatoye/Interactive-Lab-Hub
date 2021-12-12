//mindfulmirror.js

Module.register("mindfulmirror", {
	// Default module config.
	defaults: {
		msg: "Mindful Mirror",
		img_url: `https://source.unsplash.com/random/400x300?person&t=${Date.now()}`,
		fadeSpeed: 500,
		updateInterval: 5000,
		
		// smile: {
		// 	msg: "something funning",
		// 	img_url: `https://source.unsplash.com/random/400x300?happy&t=${Date.now()}`,
		// 	progress: "50%"
		// }
	},
	start: function () {
		Log.info("starting module" + this.name);
		setInterval(() => {
			Log.info("updating mirror")
			fetch(`http://${window.location.hostname}:5000`)
				.then(response => response.json())
				.then(data => {
					console.log(data);
					this.setConfig(data, true)
					this.updateDom(this.config.fadeSpeed);
				});
		}, this.config.updateInterval);
	},
	getTemplate: function () {
		return "html.njk";
	},

	getTemplateData: function () {
		return this.config;
	}

});


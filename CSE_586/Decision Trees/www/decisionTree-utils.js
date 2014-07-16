function makeTree(data, div){
	$(document).ready(function(){	
	//the data to seed the Hierarchy with
		var thisTree = data 

		// Settings up the tree - using $(selector).jstree(options);
		// All those configuration options are documented in the _docs folder
		$(div)
			.bind("select_node.jstree", function (event, data) {
				var rsltObj = data.rslt.obj;
				var facets = rsltObj[0].getAttribute("facets")
				var branch = rsltObj[0].getAttribute("parents")
				if(facets != null && branch != null){
					var facetArray = facets.split(",")
					var branchArray = branch.split(",")
					displayTips(facetArray, branchArray, eqs)
				}
		    })
            .bind("loaded.jstree", function (event, data) {
                data.inst.open_all(-1);
            })
			.jstree({ 
				// the list of plugins to include
				"plugins" : [ "themes", "json_data", "ui", "crrm", "cookies", "dnd", "search", "types", "hotkeys", "contextmenu" ],
				// Plugin configuration

				// I usually configure the plugin that handles the data first - in this case JSON as it is most common

				"json_data" : {
					"data" : thisTree
				},
				"types" : {

					// I want only `drive` nodes to be root nodes 
					// This will prevent moving or creating any other type as a root node
					"valid_children" : [ "drive" ],
					"types" : {
						// The `file` type
						"file" : {
							// can have files and other folders inside of it, but NOT `drive` nodes
							"valid_children" : "none",
							"icon" : {
								"image" : "../helpers/jsTree.v.1.0rc2/_demo/file.png"
							}
						},
						// The `folder` type
						"folder" : {
							// can have files and other folders inside of it, but NOT `drive` nodes
							"valid_children" : [ "folder", "file" ],
							"icon" : {
								"image" : "../helpers/jsTree.v.1.0rc2/_demo/folder.png"
							}
						},
						// The `drive` nodes 
						"drive" : {
							// can have files and folders inside, but NOT other `drive` nodes
							"valid_children" : [ "folder" ],
							"icon" : {
								"image" : "../helpers/jsTree.v.1.0rc2/_demo/root.png"
							},
							// those options prevent the functions with the same name to be used on the `drive` type nodes
							// internally the `before` event is used
							"start_drag" : false,
							"move_node" : false,
							"delete_node" : false,
							"remove" : false
						}
					}
				},
				"core" : { 
					// just open those two nodes up
					// as this is an AJAX enabled tree, both will be downloaded from the server
					"initially_open" : [ "root", "folder" ] 
				}
			})			
	})
}


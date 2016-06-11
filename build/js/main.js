require.config({
	baseUrl: window.location.protocol + "//" + window.location.host
	+ window.location.pathname.split("/").slice(0, -1).join("/"),

	paths: {
		ace: "/sublime-pddl/js/ace"
	}
});


require(["ace/lib/ace/ace"], function (ace) {
	var editor = ace.edit("editor");
	editor.setTheme("ace/theme/monokai");
	editor.getSession().setMode("ace/mode/javascript");
});
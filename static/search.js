function search_submit() {
	var query = $("#id_query").val();
	$("#search-results").load("/search/?ajax&query="+ encodeURIComponent(query));
	return false;
}

$(document).ready(function() {
	$("#search-form").submit(function() { search_submit();});
});
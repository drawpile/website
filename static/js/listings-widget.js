/*
Copyright (c) 2015-2017 Calle Laakkonen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
*/

(function($) {

var DEFAULT_FLAIR = '<i class="fa fa-archive"></i>';
var VERSION_FLAIR = {
	'15.6': '<span class="fa fa-archive"></span>',
	'dp:4.20.1': ' '
};

function refreshSessionList(list) {
	var tb = $("#session-list tbody");
	tb.empty();
	if(!(list instanceof Array)) {
		console.error("unexpected response, session list not an array");
		tb.append('<tr class="empty"><td colspan="5">An error occurred. Could not get session list</td>');
		return;
	}

	list = $.grep(list, function(n, i) { return n.title.length>0 });

	if(list.length>0) {
		var now = Date.now();
		for(var i=0;i<list.length;++i) {
			var s = list[i];
			var row = $('<tr></tr>');

			var flair = $('<td></td>');
			if(s.password) {
				flair.append('<i class="fa fa-key" title="Password required"></i>');
			}
			flair.append(VERSION_FLAIR[s.protocol] || DEFAULT_FLAIR);
			row.append(flair);

			var title = $('<td></td>');
			$('<a></a>')
				.attr('href', 'drawpile://' + s.host + (s.port != 27750 ? ':' + s.port : '') + '/' + s.id)
				.text(s.title)
				.appendTo(title);
			row.append(title);

			row.append($('<td></td>').text(s.owner));
			row.append($('<td></td>').text(s.users));

			var started = Date.parse(s.started.replace(' ', 'T') + "+00:00");
			var uptime = (now - started) / (1000*60);
			var hours = Math.floor(uptime / 60);
			var minutes = Math.floor(uptime - hours * 60);
			row.append($('<td></td>').text(hours + "h " + minutes + "m"));

			tb.append(row);
		}
	} else {
		tb.append('<tr class="empty"><td colspan="5">No active sessions at the moment!</td></tr>');
	}
}

$(function() {
	$("#session-list").each(function() {
		var sl = $(this);
		sl.append('<table class="session-list"><thead><tr>'+
			'<th style="width: 5px"></th>' +
			'<th>Title</th>' +
			'<th>Started by</th>' +
			'<th style="width: 40px"><i class="fa fa-users" title="Number of users"></i></th>' +
			'<th><i class="fa fa-clock-o" title="Session age"></i></th>' +
			'</tr></thead><tbody></tbody></table>');
		$.getJSON(sl.data('url'))
			.done(refreshSessionList)
			.fail(function() {
				sl.find("tbody").append('<tr class="empty"><td colspan="5">Error fetching session list</td></tr>');
			});
	});
});

})(jQuery);


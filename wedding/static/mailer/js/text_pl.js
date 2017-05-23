$(document).ready(function() {
    //rich text section
    $('.jqte').jqte({ css: "jqte_green", placeholder: "请输入内容...",
        link: false,
        unlink: false,
        titletext: [
		    { title: "Text Format | 字体格式" },
		    { title: "Font Size | 字号" },
		    { title: "Select Color | 颜色" },
		    { title: "Bold | 加粗", hotkey: "B" },
		    { title: "Italic", hotkey: "I" },
		    { title: "Underline | 下划线", hotkey: "U" },
		    { title: "Ordered List", hotkey: "." },
		    { title: "Unordered List", hotkey: "," },
		    { title: "Subscript", hotkey: "down arrow" },
		    { title: "Superscript", hotkey: "up arrow" },
		    { title: "Outdent", hotkey: "left arrow" },
		    { title: "Indent", hotkey: "right arrow" },
		    { title: "Justify Lef t| 居左" },
		    { title: "Justify Center | 居中" },
		    { title: "Justify Right | 居中" },
		    { title: "Strike Through", hotkey: "K" },
		    { title: "Add Link | 添加链接", hotkey: "L" },
		    { title: "Remove Link | 移除链接", hotkey: "" },
		    { title: "Cleaner Style", hotkey: "Delete" },
		    { title: "Horizontal Rule", hotkey: "H" },
		    { title: "Source", hotkey: "" }
	    ]
    });
});
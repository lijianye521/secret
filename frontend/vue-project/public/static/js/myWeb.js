$(function(){
    $(".content .middle ul").on("click",".switch_li",function(){
        // console.log($(this).index()) 0,1,2
        $(this).addClass("current_li").siblings().removeClass("current_li")
        $("#tittle_box").val(arr[$(this).index()])
    })
    var arr=null //标题数组
    var traitArr=null //特征图url数组
    var address=[]
    //有改动
    $("#btn_start").on("click",function(){
        $("#tittle_box").val('')
        $("#abstact_box").val('')
        $(".trait_box ul").empty()
        $(".result_hide").hide()
        $("#detail_img ul").empty()
        var abstract_len=$("#abstract_len").val()
        if(abstract_len===''){
            abstract_len=501
        }
        abstract_len=parseInt(abstract_len)
        var text=legalCheck()
        if (text){
            console.log(text) //获取的去掉空格的文本内容
            $.ajax({
               type:"POST",
                url: '/process/',
                data:{"text":text,"abstract_len":abstract_len},
                dataType:"json",
                success:function(res){
                    window.console.log(res)
                    if(res.status!==200) return alert('网络异常！')
                    else{
                        $("#abstact_box").val(res.abstract)
                        arr=res.title
                        $(".result_hide").show()
                        $(".content .middle ul .switch_li:first").click()
                        getTrait(res.analysis_graph_path)
                        traitArr=res.analysis_graph_path
                        getBigTrait(res.analysis_graph_path)
                        $("#generate_time span").text(res.times)
                        $("#abstract_len").val(res.abstract_len)
                    }
                },
                error:function(){
                    alert('ajaxError')
                },
            })
        }
    })
    window.addEventListener("load",function(){
        $.ajax({
            type:"POST",
            url: '/start/',
            data:{"text":"","abstract_len":-1},
            success:function(res){
                console.log(res)
            }
        })
    })
    function getTrait(trait){
        $.each(trait,function(i,ele){
            $.ajax({
                type:"GET",
                url:"/image_return/",
                async:false,
                data:{"image":ele},
                success:function(res){
                    var li=$("<li></li>")
                    console.log(ele)
                    li.html('<img src=data:image/png;base64,'+res+'>')
                    address.push('data:image/png;base64,'+res)
                    
                    $(".trait_box ul").append(li)
                    $(".trait_box li:first").show().siblings().hide()
                }
            })
        })
    }
    function getBigTrait(trait){
        $.each(trait,function(i,ele){
            $.ajax({
                type:"GET",
                url:"/image_return/",
                async:false,
                data:{"image":ele},
                success:function(res){
                    var li=$("<li></li>")
                    console.log(ele)
                    li.html('<img src=data:image/png;base64,'+res+'>')
                    address.push('data:image/png;base64,'+res)
                    $("#detail_img ul").append(li)
                    $("#detail_img li:first").show().siblings().hide()
                }
            })
        })
    }


    var i=1
    $(".trait_box").on("click","li",function(){
        if(i<traitArr.length){
            $(".trait_box li").eq(i).show().siblings().hide()
            i++;
        }
        else{
            i=0
            $(".trait_box li").eq(i).show().siblings().hide()
            i++
        }
        sync()
        // console.log($(".trait_box li").eq(1).index())//1
    })
    $(".trait_box").hover(function(){
        $("#detail_img").stop().fadeToggle(500)
        sync()
    })
    function sync(){
        var lismall=$(".trait_box ul")[0].children
        var libig=$("#detail_img ul")[0].children
        for(var i=0;i<traitArr.length;i++)
        {
            libig[i].style.display=lismall[i].style.display
        }
    }


    //合法性检查并且返回去掉空格的文本内容，回车前面没有句号的加上句号
    function legalCheck(){
        // 去掉所有的空格，有回车的话只保留一个
        var text=$("#text_content").val().trim().replace(/[ ]/g,'').replace(/\s+/g,'\n')
        var index=text.indexOf("\n")
        var arr=[index]
        while(index!==-1){
            index=text.indexOf('\n',index+1)
            arr.push(index)
        }
        // 从后往前添加，数组顺序才不会乱
        for(var i=arr.length-2;i>=0;i--){
            if(text[arr[i]-1]!=='。'){
                text=insertStr(text,arr[i],'。')
            }
        }
        if(text.length<30){
            alert("文本内容过短！请至少输入30字")
            return false
        }
        else {
            return text
        }
    }
    //有改动
    $(document).ajaxStart(function(){
        console.log("开始发送请求")
        $("#bg").show()
        $.ajax({
            type:"GET",
            url:"/gif/",
            data:{"gif_name":"dynamicLoad.gif"},
            success:function(res){
                $("#bgload").attr("src",'data:image/gif;base64,'+res)
                $("#bgload").show()
            }
        })
    })
    $(document).ajaxStop(function(){
        console.log("收到请求")
        $("#bg").hide().siblings("#bgload").hide()
    })

    //文件选择按钮
    $("#file").on("change",function(){
        $(".filenum span").text($(this).prop('files').length)
        // console.log($("#file").prop('files').length) //文件个数
    })
    //文件提交按钮
    $(".filebutton").on("click",function(){
        var objFile=document.querySelector("#file")
            if(objFile.value == "") {
                alert("文件不能为空")
            }
            console.log(objFile.files[0].size); // 文件字节数
            
            var files = $('#file').prop('files');//获取到文件列表
            if(files.length == 0){
                alert('请选择文件');
            }else{
                var reader = new FileReader();//新建一个FileReader
                reader.readAsText(files[0], "UTF-8");//读取文件 
                reader.onload = function(evt){ //读取完文件之后会回来这里 异步
                    var fileString = evt.target.result; // 读取文件内容
                    fileString=fileString.replace(/\\n/g,'\n')
                    console.log(fileString)
                    $("#text_content").val(fileString)
                    $(".textnum span").text($("#text_content").val().length)
                }
            }
    })
    //CLEAR按钮
    $(".clear").on("click",function(){
        $("#file").val('')
        $("#text_content").val('')
        $("#tittle_box").val('')
        $("#abstact_box").val('')
        $(".trait_box ul").empty()
        $(".result_hide").hide()
        $("#detail_img ul").empty()
        $(".filenum span").text($("#file").prop('files').length)
        $(".textnum span").text($("#text_content").val().length)
    })
    $("#text_content").on("input",function(){
        $(".textnum span").text($(this).val().length)
    })
    //下载图片
    $(".download").on("click",function(){
        var img=$(".trait_box ul")[0].children
        var a=0
        for(var i=0;i<traitArr.length;i++)
        {
            if(img[i].style.display!=="none"){
                a=i
            }
        }
        downloadImage($(".trait_box img").eq(a).prop("src"))
    })
    function downloadImage(src) {
        var a = $("<a></a>").attr("href", src).attr("download", "img.png").appendTo("body");
        a[0].click();
        a.remove();
    }
    // $("button").on("mousedown mouseup",function(){
    //     $(this).toggleClass("current_button")
    // })
    function insertStr(soure, start, newStr){   
        //start为要插入的位置
        return soure.slice(0, start) + newStr + soure.slice(start);
     }
})
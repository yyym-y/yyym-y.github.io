export default {
    point_color : "#0bbd87",

    category : [
        {key : "CSAPP", title : "CSAPP 系列", vis : false, 
        cover : "/assets/categorizeImg/CSAPP.png", firstLink : "2023/11/11/CSAPP_note1"},
        {key : "Android", title : "Android 开发系列", vis : false, 
        cover : "/assets/categorizeImg/Android.png", firstLink : "/2024/02/26/Android_note1"},
        {key : "ComputerNetwork", title : "计算机网络系列", vis : false, 
        cover : "/assets/categorizeImg/ComputerNetwork.png", firstLink : "/2024/03/30/ComputerNetwork_note6"},
        {key : "Tampermonkey", title : "油猴脚本系列", vis : false, 
        cover : "/assets/categorizeImg/Tampermonkey.png", firstLink : "/2024/04/08/Tampermonkey_note1"},
    ],
    blog : {
        CSAPP : [
            {name : "CSAPP - 信息的表示和处理", link : "/2023/11/11/CSAPP_note1", time : "2023-11-11"},
            {name : "CSAPP - 程序的机器级表示", link : "/2023/11/25/CSAPP_note2", time : "2023-11-25"},
            {name : "CSAPP - 处理器体系结构", link : "/2024/02/01/CSAPP_note3", time : "2024-02-01"},
            {name : "CSAPP - 存储器层次结构", link : "/2024/01/14/CSAPP_note4", time : "2024-01-14"},
            {name : "CSAPP - 链接", link : "/2023/12/02/CSAPP_note5", time : "2023-12-02"},
            {name : "CSAPP - 异常控制流", link : "/2023/12/13/CSAPP_note6", time : "2023-12-13"},
            {name : "CSAPP - 虚拟内存", link : "/2024/01/22/CSAPP_note7", time : "2024-01-22"}
        ],
        Android : [
            {name : "chapter1.0-安卓启程", link : "/2024/02/26/Android_note1", time : "2024-02-26"},
            {name : "chapter2.0-快速入门 Kotlin", link : "/2024/02/28/Android_note2", time : "2024-02-28"},
            {name : "chapter3.0-Activity初试", link : "2024/03/05/Android_note3", time : "2024-03-05"},
            {name : "chapter4.0-UI开发", link : "2024/04/01/Android_note4", time : "2024-04-01"},
            {name : "chapter5.0-探究Fragment", link : "2024/04/08/Android_note5/", time : "2024-04-08"}
        ],
        ComputerNetwork : [
            {name : "chapter6.0 - 物理层", link : "/2024/03/30/ComputerNetwork_note6", time : "2024-03-30"}
        ],
        Tampermonkey : [
            {name : "第一个 Tampermonkey 脚本", link : "/2024/04/08/Tampermonkey_note1", time : "2024-04-08"}
        ]
    }
}
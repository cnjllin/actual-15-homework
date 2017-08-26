<map version="1.0.1">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node CREATED="1503194200286" ID="ID_586651278" MODIFIED="1503403315119" TEXT="05MVC/&#x6570;&#x636e;&#x5e93;">
<node CREATED="1503194209646" ID="ID_1876437290" MODIFIED="1503194264035" POSITION="right" TEXT="M --&#x6570;&#x636e;&#x5b58;&#x50a8;&#xff0c;&#x5fc3;&#x6cd5;-&#x589e;&#x5220;&#x6539;&#x67e5;"/>
<node CREATED="1503194266677" ID="ID_215820769" MODIFIED="1503194433275" POSITION="right" TEXT="&#x5c06;M&#x7aef;&#x6570;&#x636e;&#x62ff;&#x5230;&#x5e76;&#x5904;&#x7406;&#x597d;&#xff0c;&#x7136;&#x540e;&#x8f6c;&#x7ed9;&#x524d;&#x7aef;V"/>
<node CREATED="1503194345857" ID="ID_769384073" MODIFIED="1503194392130" POSITION="right" TEXT="&#x63a5;&#x53d7;&#x524d;&#x7aef;&#x6570;&#x636e;&#xff0c;&#x7136;&#x540e;&#x5904;&#x7406;&#x597d;&#xff0c;&#x4ea4;&#x7ed9;&#x5b58;&#x50a8;M"/>
<node CREATED="1503194438013" ID="ID_429487255" MODIFIED="1503194469461" POSITION="right" TEXT="V--&#x524d;&#x7aef;&#x4ee3;&#x7801;&#xff0c;HTML/CSS/JS">
<node CREATED="1503194471476" ID="ID_1812967042" MODIFIED="1503194526514" TEXT="&#x63d0;&#x4f9b;&#x7528;&#x6237;&#x8f93;&#x5165;&#x6570;&#x636e;&#x7684;&#x63a5;&#x53e3;&#xff0c;&#x4f8b;&#x5982;&#xff1a;&#x8868;&#x5355;"/>
<node CREATED="1503194473608" ID="ID_1028780486" MODIFIED="1503194473608" TEXT=""/>
</node>
<node CREATED="1503211088674" ID="ID_1785236835" MODIFIED="1503211106679" POSITION="right" TEXT="&#x4f7f;&#x7528;&#x573a;&#x666f;">
<node CREATED="1503211108021" ID="ID_713802825" MODIFIED="1503211121865" TEXT="GET&#xff1a;&#x5bf9;&#x6570;&#x636e;&#x7684;&#x67e5;&#xff0c;&#x5220;"/>
<node CREATED="1503211122722" ID="ID_1313623712" MODIFIED="1503211148663" TEXT="POST&#xff1a;&#x5bf9;&#x6570;&#x636e;&#x7684;&#x589e;&#xff0c;&#x6539;"/>
</node>
<node CREATED="1503220395651" ID="ID_1101048419" MODIFIED="1503220398989" POSITION="right" TEXT="mysql">
<node CREATED="1503220400876" ID="ID_191488599" MODIFIED="1503220626959">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      &#21019;&#24314;&#25968;&#25454;&#24211;
    </p>
    <p>
      &gt; create database reboot15 CHARACTER SET utf8&#160;&#160;COLLATE utf8_general_ci;
    </p>
    <p>
      &gt; use reboot15;
    </p>
    <p>
      &gt; CREATE TABLE `user` (`id` int(100) NOT NULL AUTO_INCREMENT,
    </p>
    <p>
      `username` varchar(100) NOT NULL,
    </p>
    <p>
      `password` varchar(100) NOT NULL,
    </p>
    <p>
      `sex` int(10) DEFAULT NULL,
    </p>
    <p>
      `age` int(10) DEFAULT NULL,
    </p>
    <p>
      `phone` int(11) DEFAULT NULL,
    </p>
    <p>
      &#160;`email` varchar(100) DEFAULT NULL,
    </p>
    <p>
      `role` int(10) DEFAULT NULL,
    </p>
    <p>
      PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    </p>
    <p>
      
    </p>
    <p>
      &gt; insert into user values (1, 'chw', '123456', 0, 18, 18701541185, 'chw@reboot.com', 0);
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1503220652072" ID="ID_71226927" MODIFIED="1503491323575" TEXT="import MySQLdb as mysql&#xa;db = mysql.connect(host=&apos;127.0.0.1&apos;,user=&apos;root&apos;,passwd=&apos;123456&apos;,db=&apos;reboot15&apos;,port=3306,charset=&apos;utf8&apos;)&#xa;cur = db.cursor()&#xa;sql = &apos;select * from user&apos;&#xa;cur.execute(sql)&#xa;ss = cur.fetchall()&#xa;&#xa;"/>
<node CREATED="1503223706362" ID="ID_31926827" MODIFIED="1503540827784">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      1,&#23548;&#20837;&#27169;&#22359;
    </p>
    <p>
      2&#65292;&#36830;&#24211;&#160;&#160;&#160;,db.autocommit(True) &#33258;&#21160;&#25552;&#20132;&#25968;&#25454;
    </p>
    <p>
      3&#65292;&#28216;&#26631;&#160;&#160;cur = db.cursor()
    </p>
    <p>
      &#23450;&#20041; sql&#35821;&#21477;
    </p>
    <p>
      cur.execute(sql)
    </p>
    <p>
      ss = cur.fetchall()
    </p>
  </body>
</html>
</richcontent>
</node>
</node>
<node CREATED="1503195863949" ID="ID_1095119495" MODIFIED="1503195882288" POSITION="left">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      M&#160;&#160;&#22686;&#21024;&#25913;&#26597;&#65292;--&#25991;&#20214;&#12289;&#25968;&#25454;&#24211; &#23384;&#20648;
    </p>
    <p>
      V&#160;&#160;&#21069;&#31471; --Html/CSS/JS
    </p>
    <p>
      C&#160;&#160;if else ,for&#160;&#160;in ,&#20195;&#30721;
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1503201079347" ID="ID_104350104" MODIFIED="1503202828321" POSITION="left">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p>
      import&#160;redirect
    </p>
  </body>
</html></richcontent>
<node CREATED="1503201144935" ID="ID_1814838836" MODIFIED="1503490459102" TEXT="return redirect(&apos;/login&apos;/) &#x8df3;&#x8f6c;"/>
</node>
<node CREATED="1503202830930" ID="ID_1354929855" MODIFIED="1503202841449" POSITION="left" TEXT="&#x9519;&#x8bef;&#x4fe1;&#x606f;">
<node CREATED="1503202842909" ID="ID_638646658" MODIFIED="1503490532210">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <div style="text-align: left">
      res_code = u'&#30331;&#24405;&#25104;&#21151;'&#160; &#160;return render_template(&quot;login1.html&quot;,res_code = res_code)<br />&#21464;&#37327;&#23450;&#20041;&#38169;&#35823;&#20449;&#24687;&#160;&#28982;&#21518;&#20256;&#21040;&#21069;&#31471;&#28210;&#26579;<br /><br />
    </div>
  </body>
</html>
</richcontent>
</node>
</node>
</node>
</map>

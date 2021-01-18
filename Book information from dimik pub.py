import re
s="""
<div class="book-cover">

					 <a href="http://dimik.pub/book/400/becoming-a-problem-solver-by-munem-ruhul"><img src="http://dimik.pub/wp-content/uploads/2019/01/hoye-otho-ekjon-problem-solver-front-cover-350X450-.png"></a>
                </div><!-- end .book-cover -->

                <div class="slide-description">
                    <div class="inner-sd">
                        <div class="top-sd-head clearfix">
                            <div class="tsh-left">
                            <h2 class="sd-title"><a href="http://dimik.pub/book/400/becoming-a-problem-solver-by-munem-ruhul">হয়ে ওঠো একজন প্রবলেম সলভার</a></h2>
"""
regexp=re.compile(r'<div class="book-cover">\s*<a href="(.*?)"><img src="(.*?)">.*?<h2 class="sd-title"><.*?>(.*?)<',re.S)
result=re.findall(regexp,s)
print(result)

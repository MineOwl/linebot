from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import datetime



def get_tweet_time(self):
    tweet_num = get_tweet_num()
    while True:
        if tweet_num == get_tweet_num():
            pass
        else:
            self.last = datetime.datetime.now()
        time.sleep(5)
        tweet_num = get_tweet_num()


def get_tweet_num(*,acount="mswn7"):
    html = urlopen("https://twitter.com/mswn7?lang=ja")
    bsObj = BeautifulSoup(html,"lxml")
    text = bsObj.find("span",{"class","ProfileNav-value"})
    return text.attrs['data-count']





"""
"><span class="u-hidden">非公開ツイート</span></span></span>
</div>
<div class="ProfileCardMini-screenname">
<a class="ProfileCardMini-screennameLink u-linkComplex js-nav u-dir" dir="ltr" href="/mswn7">
<span class="username u-dir" dir="ltr">@<b class="u-linkComplex-target">mswn7</b></span>
</a>
</div>
</div>
</div>
</div>
</div>
<div class="Grid-cell u-size2of3 u-lg-size3of4">
<div class="ProfileCanopy-nav">
<div class="ProfileNav" data-user-id="1629466554" role="navigation">
<ul class="ProfileNav-list">
<li class="ProfileNav-item ProfileNav-item--tweets is-active">
<a class="ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-nav" data-nav="tweets" tabindex="0" title="2,676ツイート">
<span aria-hidden="true" class="ProfileNav-label">ツイート</span>
<span class="u-hiddenVisually">ツイート、現在のページ。</span>
<span class="ProfileNav-value" data-count="2676" data-is-compact="false">2,676
            </span>
</a>
</li><li class="ProfileNav-item ProfileNav-item--following">
<a class="ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor" data-nav="following" href="/mswn7/following" title="594人をフォロー中">
<span aria-hidden="true" class="ProfileNav-label">フォロー</span>
<span class="u-hiddenVisually">フォロー</span>
<span class="ProfileNav-value" data-count="594" data-is-compact="false">594</span>
</a>
</li><li class="ProfileNav-item ProfileNav-item--followers">
<a class="ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor" data-nav="followers" href="/mswn7/followers" title="179人のフォロワー">
<span aria-hidden="true" class="ProfileNav-label">フォロワー</span>
<span class="u-hiddenVisually">フォロワー</span>
<span class="ProfileNav-value" data-count="179" data-is-compact="false">179</span>
</a>
</li><li class="ProfileNav-item ProfileNav-item--favorites" data-more-item=".ProfileNav-dropdownItem--favorites">
<a class="ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor" data-nav="favorites" href="/mswn7/likes" title="4,773いいね">
<span aria-hidden="true" class="ProfileNav-label">いいね</span>
<span class="u-hiddenVisually">いいね</span>
<span class="ProfileNav-value" data-count="4773" data-is-compact="false">4,773</span>
</a>
</li><li class="ProfileNav-item ProfileNav-item--lists" data-more-item=".ProfileNav-dropdownItem--lists">
<a class="ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor" data-nav="all_lists" href="/mswn7/lists" title="1件のリスト">
<span aria-hidden="true" class="ProfileNav-label">リスト</span>
<span class="u-hiddenVisually">リスト</span>
<span class="ProfileNav-value" data-is-compact="false">1</span>
</a></li><li class="ProfileNav-item ProfileNav-item--more dropdown is-hidden"> <a class="ProfileNav-stat ProfileNav-stat--link ProfileNav-stat--moreLink js-openSignupDialog js-nonNavigable" href="#more" role="button">
<span class="ProfileNav-label"> </span>
<span class="ProfileNav-value">その他 <span class="ProfileNav-dropdownCaret Icon Icon--medium Icon--caretDown"></span></span>
</a>
<div class="dropdown-menu">
<div class="dropdown-caret">
<span class="caret-outer"></span>
<span class="caret-inner"></span>
</div>

"""
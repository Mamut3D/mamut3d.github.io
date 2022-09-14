+++
title = "GitHub pages"
+++

## Obsolete - GitHub pages with jekyll

- [Repo prep](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll)
- [Local jekyll test](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)
  - download gems `cd docs && bundle install`
  - Test locally on termux requires fix at `vim /data/data/com.termux/files/usr/lib/ruby/gems/3.1.0/gems/jekyll-3.9.2/lib/jekyll/utils/platforms.rb` according to <https://github.com/jekyll/jekyll/issues/7045>
  - also one more fix all ready present in this repo Gemfile <https://github.com/jekyll/jekyll/issues/8523>
  - serve pages locally `bundle exec jekyll serve --host 0.0.0.0.`

import scrapy


class UnicodeEmojiSpider(scrapy.Spider):
    name = "unicode_emoji"
    allowed_domains = ['unicode.org']
    start_urls = ['https://unicode.org/emoji/charts/full-emoji-list.html']

    def parse(self, response):
        group_name = None
        group = []
        trs = response.css("tr")
        for tr in trs:
            if tr.css("th.mediumhead"):
                if group_name is not None:
                    yield {"group_name": group_name, "group": group}
                group_name = tr.css("th.mediumhead > a::text").get()
                group.clear()
            elif tr.css("td.code"):
                code: str = tr.css("td.code > a::text").get()
                code: list = list(map(lambda x: x[2:], code.split()))
                name = tr.css("td.name::text").get()
                group.append({"code": code, "name": name})
        return {"group_name": group_name, "group": group}

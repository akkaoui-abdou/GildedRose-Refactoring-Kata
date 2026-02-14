# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def increase_quality(self, item, amount):
        item.quality = min(50, item.quality + amount)

    def decrease_quality(self, item, amount):
        item.quality = max(0, item.quality - amount)

    def update_quality(self):
        for item in self.items:
            name = item.name
            is_sulfuras = name == "Sulfuras, Hand of Ragnaros"
            is_aged_brie = name == "Aged Brie"
            is_backstage_passes = (
                name == "Backstage passes to a TAFKAL80ETC concert"
            )
            is_conjurd = "Conjured" in name
            # ---------------------------
            # Legendary Item: Sulfuras
            # ---------------------------
            if is_sulfuras:
                continue
            # decrease sell_in for all non-Sulfuras
            item.sell_in -= 1
            if is_aged_brie:
                self.increase_quality(item, 1)
                if item.sell_in < 0:
                    self.increase_quality(item, 1)
            elif is_backstage_passes:
                if item.sell_in < 0:
                    item.quality = 0
                else:
                    if item.sell_in <= 5:
                        amount = 3
                    elif item.sell_in <= 10:
                        amount = 2
                    else:
                        amount = 1
                    self.increase_quality(item, amount)
            else:
                # ---------------------------
                # Normal items (including Conjured)
                # ---------------------------
                amount = 2 if is_conjurd else 1
                self.decrease_quality(item, amount)
                if item.sell_in < 0:
                    self.decrease_quality(item, amount)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

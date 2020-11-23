#!/usr/bin/python3
# @Time    : 2020-11-23
# @Author  : Kevin Kong (kfx2007@163.com)

import unittest
from oms.api import OMS


class TestComm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.oms = OMS("bvW2Fcx8Hb1OYzZaL2mY8A==",
                      "Pa2zfPtcCIvmhxYkfw5Bj6JgPmx63s4i")

    def test_define_product(self):
        """Test Comm"""
        res = self.oms.product.define_product("COMMONCOMPANY", [
            {"Item": {
                "SkuNo": "1111",
                "ItemName": "2222"
            }}
        ])
        self.assertEqual(res['result'],0,res)


if __name__ == "__main__":
    unittest.main()

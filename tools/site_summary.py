# tools/site_summary.py
# -*- coding: utf-8 -*-

import json
import datetime
from collections import OrderedDict


SITE_DATA = [
    OrderedDict([
        ("title", "乐鱼体育 - 首页"),
        ("url", "https://index-main-leyusports.com.cn"),
        ("keywords", ["乐鱼体育", "体育平台", "在线娱乐"]),
        ("description", "乐鱼体育官方主站，提供丰富的体育赛事资讯与娱乐服务。"),
        ("category", "体育门户"),
        ("language", "zh-CN")
    ]),
    OrderedDict([
        ("title", "乐鱼体育 - 赛事中心"),
        ("url", "https://index-main-leyusports.com.cn/events"),
        ("keywords", ["体育赛事", "比分直播", "乐鱼体育"]),
        ("description", "实时更新全球体育赛事信息，包括足球、篮球、网球等多种项目。"),
        ("category", "赛事服务"),
        ("language", "zh-CN")
    ]),
    OrderedDict([
        ("title", "乐鱼体育 - 用户帮助"),
        ("url", "https://index-main-leyusports.com.cn/help"),
        ("keywords", ["帮助中心", "乐鱼体育", "客服支持"]),
        ("description", "提供常见问题解答、账户安全指南及联系方式。"),
        ("category", "支持中心"),
        ("language", "zh-CN")
    ])
]


def format_list(items, separator=", "):
    """将列表格式化为字符串"""
    return separator.join(items)


def create_summary_entry(site_info):
    """为单个站点生成结构化摘要"""
    entry = OrderedDict()
    entry["名称"] = site_info.get("title", "未命名")
    entry["地址"] = site_info.get("url", "")
    entry["标签"] = format_list(site_info.get("keywords", []))
    entry["简介"] = site_info.get("description", "")
    entry["分类"] = site_info.get("category", "")
    entry["语言"] = site_info.get("language", "")
    return entry


def generate_summary_text(sites):
    """生成完整摘要文本"""
    lines = []
    lines.append("=" * 60)
    lines.append("  站点摘要报告")
    lines.append("  生成时间: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    lines.append("=" * 60)
    lines.append("")

    for index, site in enumerate(sites, start=1):
        entry = create_summary_entry(site)
        lines.append(f"【条目 {index}】")
        for key, value in entry.items():
            lines.append(f"  {key}: {value}")
        lines.append("")

    lines.append("-" * 60)
    lines.append(f"共收录 {len(sites)} 个站点页面")
    lines.append("=" * 60)
    return "\n".join(lines)


def export_as_json(sites, indent=2):
    """导出结构化摘要为JSON格式"""
    result = []
    for site in sites:
        entry = create_summary_entry(site)
        result.append(entry)
    return json.dumps(result, ensure_ascii=False, indent=indent)


def main():
    """主函数：生成并输出摘要"""
    text_summary = generate_summary_text(SITE_DATA)
    print(text_summary)
    print("\n")
    print("【JSON 格式输出】")
    print(export_as_json(SITE_DATA))


if __name__ == "__main__":
    main()
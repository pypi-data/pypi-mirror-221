def parse_company_industry_tag(tags):
    industry_tag = tags.get("industry_tag", [])
    tag_info = {
        "type": "产业标签",
        "tags": []
    }
    if industry_tag:
        for _ in industry_tag:
            if _:
                tag_name = _.get("tag_name")
                if tag_name:
                    tag_info["tags"].append(tag_name)
    return tag_info


def parse_company_permission_level_tag(tags):
    permission = tags.get("permission", [])
    tag_info = {
        "type": "备案许可级别",
        "tags": []
    }
    if permission:
        for _ in permission:
            if _:
                level = _.get("level")
                if level:
                    tag_info["tags"].append(level)
    return tag_info


def parse_company_permission_name_tag(tags):
    permission = tags.get("permission", [])
    tag_info = {
        "type": "备案许可名称",
        "tags": []
    }
    if permission:
        for _ in permission:
            if _:
                permission_name = _.get("permission_name")
                if permission_name:
                    tag_info["tags"].append(permission_name)
    return tag_info


def parse_company_certification_tag(tags):
    certification = tags.get("certification", [])
    tag_info = {
        "type": "资质认证名称",
        "tags": []
    }
    if certification:
        for _ in certification:
            if _:
                certification_name = _.get("certification_name")
                if certification_name:
                    tag_info["tags"].append(certification_name)
    return tag_info


def parse_company_award_tag(tags):
    award_tag = tags.get("award_tag", [])
    tag_info = {
        "type": "奖项名称",
        "tags": []
    }
    if award_tag:
        for _ in award_tag:
            if _:
                tag_name = _.get("tag_name")
                if tag_name:
                    tag_info["tags"].append(tag_name)
    return tag_info


def parse_company_rank_tag(tags):
    rank_tag = tags.get("rank_tag", [])
    tag_info = {
        "type": "榜单名称",
        "tags": []
    }
    if rank_tag:
        for _ in rank_tag:
            if _:
                rank_name = _.get("rank_name")
                if rank_name:
                    tag_info["tags"].append(rank_name)
    return tag_info


def parse_company_diy_tag(tags):
    diy_tag = tags.get("diy_tag", [])
    tag_info = {
        "type": "diy标签",
        "tags": []
    }
    if diy_tag:
        for _ in diy_tag:
            if _:
                tag_info["tags"].append(_)
    return tag_info


def parse_company_tag(tags: dict, return_type: bool = False, tag_type_list: list = None):
    _tags = []
    tag_list = [parse_company_industry_tag(tags),
                parse_company_permission_level_tag,
                parse_company_permission_name_tag,
                parse_company_certification_tag,
                parse_company_award_tag,
                parse_company_rank_tag,
                parse_company_diy_tag
                ]

    if tag_type_list and return_type:
        for x in tag_list:
            if x in tag_type_list:
                _tags.append(x)
    elif tag_type_list and not return_type:
        for x in tag_list:
            if x in tag_type_list:
                _ = x.get("tags")
                if _:
                    _tags.extend(_)
    elif not tag_type_list and return_type:
        _tags = tag_list
    else:
        for x in tag_list:
            _ = x.get("tags")
            if _:
                _tags.extend(_)

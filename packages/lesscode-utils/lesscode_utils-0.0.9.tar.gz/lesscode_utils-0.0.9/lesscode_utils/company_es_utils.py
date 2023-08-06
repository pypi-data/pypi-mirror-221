def parse_company_industry_tag(tags):
    tag_list = []
    industry_tag = tags.get("industry_tag", [])
    if industry_tag:
        for _ in industry_tag:
            if _:
                tag_name = _.get("tag_name")
                if tag_name:
                    tag_list.append(tag_name)
    return tag_list


def parse_company_permission_level_tag(tags):
    permission = tags.get("permission", [])
    tag_list = []
    if permission:
        for _ in permission:
            if _:
                level = _.get("level")
                if level:
                    tag_list.append(level)
    return tag_list


def parse_company_permission_name_tag(tags):
    permission = tags.get("permission", [])
    tag_list = []
    if permission:
        for _ in permission:
            if _:
                permission_name = _.get("permission_name")
                if permission_name:
                    tag_list.append(permission_name)
    return tag_list


def parse_company_certification_tag(tags):
    certification = tags.get("certification", [])
    tag_list = []
    if certification:
        for _ in certification:
            if _:
                certification_name = _.get("certification_name")
                if certification_name:
                    tag_list.append(certification_name)
    return tag_list


def parse_company_award_tag(tags):
    award_tag = tags.get("award_tag", [])
    tag_list = []
    if award_tag:
        for _ in award_tag:
            if _:
                tag_name = _.get("tag_name")
                if tag_name:
                    tag_list.append(tag_name)
    return tag_list


def parse_company_rank_tag(tags):
    rank_tag = tags.get("rank_tag", [])
    tag_list = []
    if rank_tag:
        for _ in rank_tag:
            if _:
                rank_name = _.get("rank_name")
                if rank_name:
                    tag_list.append(rank_name)
    return tag_list


def parse_company_diy_tag(tags):
    diy_tag = tags.get("diy_tag", [])
    tag_list = []
    if diy_tag:
        for _ in diy_tag:
            if _:
                tag_list.append(_)
    return tag_list


def parse_company_tag(tags: dict, return_type: bool = False, tag_type_list: list = None):
    _tags = []
    tag_dict = {
        "产业标签": parse_company_industry_tag,
        "备案许可级别": parse_company_permission_level_tag,
        "备案许可名称": parse_company_permission_name_tag,
        "资质认证名称": parse_company_certification_tag,
        "奖项名称": parse_company_award_tag,
        "榜单名称": parse_company_rank_tag,
        "diy标签": parse_company_diy_tag
    }
    if tag_type_list:
        for tag_type in tag_dict:
            if tag_type in tag_type_list and tag_type in tag_dict:
                if not return_type:
                    _tags.extend(tag_dict.get(tag_type)(tags))
                else:
                    tag_info = {
                        "tag_type": tag_type,
                        "tags": tag_dict.get(tag_type)(tags)
                    }
                    _tags.append(tag_info)
    else:
        for tag_type in tag_dict:
            if tag_type in tag_dict:
                if not return_type:
                    _tags.extend(tag_dict.get(tag_type)(tags))
                else:
                    tag_info = {
                        "tag_type": tag_type,
                        "tags": tag_dict.get(tag_type)(tags)
                    }
                    _tags.append(tag_info)
    return _tags

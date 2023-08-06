# encoding: utf-8
"""
@project: djangoModel->user_relate_service
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 用户关系服务
@created_time: 2022/12/13 16:45
"""
from django.core.paginator import Paginator, EmptyPage
from django.db.models import F

from xj_role.services.role_service import RoleService
from ..models import UserRelateType, UserRelateToUser, BaseInfo
from ..services.user_detail_info_service import DetailInfoService
# 用户关系类型服务
from ..utils.custom_tool import format_params_handle, force_transform_type, filter_fields_handler, dynamic_load_class


class UserRelateTypeService():
    @staticmethod
    def list(params=None):
        if params is None:
            params = {}
        size = params.get("size", 10)
        page = params.get("page", 20)
        filter_params = format_params_handle(
            param_dict=params,
            filter_filed_list=["id", "relate_key", "relate_name", ]
        )
        relate_obj = UserRelateType.objects.filter(**filter_params).values()
        count = relate_obj.count()
        page_set = Paginator(relate_obj, size).get_page(page)
        return {'count': count, "page": page, "size": size, "list": list(page_set.object_list)}, None

    @staticmethod
    def add(params=None):
        if params is None:
            params = {}
        filter_params = format_params_handle(
            param_dict=params,
            filter_filed_list=["relate_key", "relate_name", "description", "is_multipeople"]
        )
        try:
            relate_obj = UserRelateType.objects.create(**filter_params)
            return {"id": relate_obj.id}, None
        except Exception as e:
            return None, str(e)

    @staticmethod
    def edit(pk=None, update_params=None):
        if update_params is None:
            update_params = {}
        filter_params = format_params_handle(
            param_dict=update_params,
            filter_filed_list=["relate_key", "relate_name", "description", "is_multipeople"]
        )
        if not pk or not filter_params:
            return None, "没有可修改的数据"
        try:
            relate_obj = UserRelateType.objects.filter(id=pk)
            if not relate_obj:
                return None, "没有可修改的数据"
            relate_obj.update(**filter_params)

            return None, None
        except Exception as e:
            return None, str(e)

    @staticmethod
    def delete(pk=None):
        if not pk:
            return None, "参数错误"
        relate_obj = UserRelateType.objects.filter(id=pk)
        if not relate_obj:
            return None, None
        try:
            relate_obj.delete()
        except Exception as e:
            return None, "删除异常:" + str(e)
        return None, None


# 用户关系映射服务
class UserRelateToUserService():
    @staticmethod
    def list(params=None, filter_fields=None, only_first=False, **kwargs):
        """
        查询用户关系映射
        :param params: 参数
        :param filter_fields: 过滤字段
        :param only_first: 仅仅查询第一条
        """
        # ------------------------- section 参数处理 start ------------------------------------
        params, err = force_transform_type(variable=params, var_type="dict", default={})
        size, err = force_transform_type(variable=params.get("size"), var_type="int", default=10)
        page, err = force_transform_type(variable=params.get("page"), var_type="int", default=1)
        need_pagination, err = force_transform_type(variable=params.get("need_pagination"), var_type="bool", default=True)
        sort = params.get("sort")
        sort = sort if sort and sort in ["created_time", "-created_time", "id", "-id"] else "-created_time"
        default_field_list = [
            "user_id", "with_user_id", "user_relate_type_id", "relate_key", "relate_type_name",
            "user_name", "full_name", "nickname", "with_user_name", "with_full_name", "with_nickname",
            "created_time"
        ]
        filter_fields = filter_fields_handler(
            input_field_expression=filter_fields,
            default_field_list=default_field_list,
            all_field_list=default_field_list + ["user_phone", "with_user_phone"]
        )
        filter_params = format_params_handle(
            param_dict=params,
            filter_filed_list=[
                "user_id|int", "user_id_list", "with_user_id|int", "user_relate_type_id|int", "relate_key",
                "user_name", "full_name", "nickname", "with_user_name", "with_full_name", "with_nickname",
                "created_time_start", "created_time_end"
            ],
            alias_dict={
                "user_id_list": "user_id__in", "with_user_id_list": "with_user_id__in",
                "created_time_start": "created_time__gte", "created_time_end": "created_time__lte"
            },
            split_list=["user_id_list", "with_user_id_list"]
        )
        # ------------------------- section 参数处理 end   ------------------------------------

        # ------------------------- section 构建ORM start ------------------------------------
        relate_user_obj = UserRelateToUser.objects.extra(
            select={"created_time": 'DATE_FORMAT(created_time, "%%Y-%%m-%%d %%H:%%i:%%s")'}
        ).annotate(
            relate_key=F("user_relate_type__relate_key"),
            relate_type_name=F("user_relate_type__relate_name"),
            user_name=F("user__user_name"),
            user_phone=F("user__phone"),
            full_name=F("user__full_name"),
            nickname=F("user__nickname"),
            with_user_name=F("with_user__user_name"),
            with_user_phone=F("with_user__phone"),
            with_full_name=F("with_user__full_name"),
            with_nickname=F("with_user__nickname")
        ).filter(**filter_params).order_by(sort).values(*filter_fields)
        # ------------------------- section 构建ORM end ------------------------------------

        # ------------------------- section 构建返回体 start ------------------------------------
        # 单条返回
        if only_first:
            return relate_user_obj.first(), None

        # 列表返回
        total = relate_user_obj.count()
        if not need_pagination and total <= 200:
            return list(relate_user_obj), None

        # 分页返回
        else:
            try:
                page_set = Paginator(relate_user_obj, size).page(page)
            except EmptyPage:
                return {'total': total, "page": page, "size": size, "list": []}, None
            return {'total': total, "page": page, "size": size, "list": list(page_set.object_list)}, None
        # ------------------------- section 构建返回体 end   ------------------------------------

    @staticmethod
    def add(params: dict = None, **kwargs):
        params, is_pass = force_transform_type(variable=params, var_type="dict", default={})
        kwargs, is_pass = force_transform_type(variable=kwargs, var_type="dict", default={})
        params.update(kwargs)

        # ------------------- section 获取关系类型 start ---------------------------
        relate_key = params.get("user_relate_type_value", params.get("relate_key"))
        if relate_key:
            user_relate_type = UserRelateType.objects.filter(relate_key=relate_key).values().first()
        else:
            user_relate_type = UserRelateType.objects.filter(id=params.get("user_relate_type_id")).values().first()
        if not user_relate_type:
            return None, "不是有效的关系类型"
        params.setdefault("user_relate_type_id", user_relate_type.get("id"))
        # ------------------- section 获取关系类型 end   ---------------------------

        # ------------------- section 过滤字段,并校验合法性 start ---------------------------
        # 参数处理
        filter_params = format_params_handle(
            param_dict=params,
            filter_filed_list=["user", "user_id", "with_user", "with_user_id", "user_relate_type", "user_relate_type_id"],
            alias_dict={"user": 'user_id', "with_user": "with_user_id", "user_relate_type": "user_relate_type_id"}
        )
        if filter_params.get("user_id", None) is None or filter_params.get("with_user_id", None) is None or filter_params.get("user_relate_type_id", None) is None:
            return None, "参数错误"
        # ------------------- section 过滤字段,并校验合法性 end   ---------------------------

        # ------------------- section 判断是否可以重复绑定 start ---------------------------
        if user_relate_type.get("is_multipeople"):
            # 检查是否已经绑定过
            relate_user_obj = UserRelateToUser.objects.filter(
                user_id=filter_params['user_id'],
                with_user=filter_params['with_user_id'],
                user_relate_type_id=filter_params['user_relate_type_id']
            ).first()
        else:
            # 可多人绑定的用户关系
            relate_user_obj = UserRelateToUser.objects.filter(
                user_id=filter_params['user_id'],
                user_relate_type_id=filter_params['user_relate_type_id']
            ).first()
        if relate_user_obj:
            return None, "无法重复绑定，或者该关系类型不是多人绑定类型。"
        # ------------------- section 判断是否可以重复绑定 end   ---------------------------

        # ------------------- section IO操作 start ---------------------------
        try:
            relate_user_obj = UserRelateToUser.objects.create(**filter_params)
            return {"id": relate_user_obj.id}, None
        except Exception as e:
            return None, str(e)
        # ------------------- section IO操作 end   ---------------------------

    @staticmethod
    def edit(pk=None, params=None):
        if params is None:
            params = {}
        filter_params = format_params_handle(
            param_dict=params,
            filter_filed_list=["user", "user_id", "with_user", "with_user_id", "user_relate_type", "user_relate_type_id"],
            alias_dict={"user": 'user_id', "with_user": "with_user_id", "user_relate_type": "user_relate_type_id"}
        )
        if not pk or not params:
            return None, "没有可修改的数据"

        try:
            relate_user_obj = UserRelateToUser.objects.filter(id=pk)
            if not relate_user_obj:
                return None, "没有可修改的数据"
            relate_user_obj.update(**filter_params)
            return None, None
        except Exception as e:
            return None, str(e)

    @staticmethod
    def delete(pk=None):
        if not pk:
            return None, "参数错误"
        relate_user_obj = UserRelateToUser.objects.filter(id=pk)
        if not relate_user_obj:
            return None, None
        try:
            relate_user_obj.delete()
        except Exception as e:
            return None, "删除异常:" + str(e)
        return None, None

    @staticmethod
    def bind_bxtx_relate(params: dict = None, user_info: dict = None, **kwargs):
        """
        镖行天下绑定用户关系服务
        @note  绑定用户关系 邀请关系和收益关系
        :param params: 请求参数
        :param user_info: 用户信息
        :return: None,err_msg
        """
        user_info, is_pass = force_transform_type(variable=user_info, var_type="dict", default={})
        kwargs, is_pass = force_transform_type(variable=kwargs, var_type="dict", default={})
        params, is_pass = force_transform_type(variable=params, var_type="dict", default={})
        params.update(user_info)
        params.update(kwargs)
        # 获取绑定用户关系
        user_id, is_pass = force_transform_type(variable=params.get('user_id', params.get('id')), var_type="int", default=0)  # 当前用户ID
        inviter_id, is_pass = force_transform_type(variable=params.get('inviter_id'), var_type="int", default=0)  # 邀请人ID
        try:
            # 判断是否是一个有效的用户ID
            inviter = BaseInfo.objects.filter(id=inviter_id).first()
            if not inviter:
                return None, None

            # 绑定邀请人
            data, err = UserRelateToUserService.add({
                "user_id": user_id,
                "with_user_id": inviter_id,
                "user_relate_type_value": "invite"
            })
            if err:
                return None, None

            # 邀请人不存在受益人，如果邀请人是业务，则绑定的受益人也是该邀请人
            res, err = RoleService.is_this_role(user_id=inviter_id, role_key="BID-SALESMAN")  # 如果是业务人员
            if res:
                data, err = UserRelateToUserService.add({
                    "user_id": user_id,
                    "with_user_id": inviter_id,
                    "user_relate_type_value": "beneficiary"
                })
                return None, err

            # 查询邀请人的受益人是谁，如果存在则绑定。
            saler = UserRelateToUser.objects.annotate(relate_key=F("user_relate_type__relate_key")).filter(
                user_id=inviter_id, relate_key="beneficiary"
            ).values().first()
            if saler:
                data, err = UserRelateToUserService.add({
                    "user_id": user_id,
                    "with_user_id": saler.get("with_user_id"),
                    "user_relate_type_value": "beneficiary"
                })
                return None, None

        except Exception as e:
            return None, str(e)
        return None, None

    @staticmethod
    def bxtx_relate_user(*args, params: dict = None, **kwargs):
        """
        查询用户关系映射
        :param params: 参数
        """
        # ------------------------- section 参数处理 start ------------------------------------
        kwargs, err = force_transform_type(variable=kwargs, var_type="only_dict", default={})
        params, err = force_transform_type(variable=params, var_type="only_dict", default={})
        params.update(kwargs)

        direct_invite, err = force_transform_type(variable=params.get("direct_invite"), var_type="bool", default=True)
        select_all, err = force_transform_type(variable=params.get("select_all"), var_type="bool", default=False)
        relate_key = "invite" if direct_invite else "beneficiary"
        relate_key = "beneficiary" if select_all else relate_key

        user_id, err = force_transform_type(variable=params.get("user_id"), var_type="int")
        if not user_id:
            return None, "不是一个有效的 user_id"
        relate_key, err = force_transform_type(variable=relate_key, var_type="str", default="invite")
        size, err = force_transform_type(variable=params.pop('size', 10), var_type="int", default=10)
        page, err = force_transform_type(variable=params.pop('page', 1), var_type="int", default=1)
        # ------------------------- section 参数处理 end   ------------------------------------

        # ------------------------- section 构建ORM start ------------------------------------
        relate_user_obj = UserRelateToUser.objects.extra(
            select={"created_time": 'DATE_FORMAT(created_time, "%%Y-%%m-%%d %%H:%%i:%%s")'}
        ).annotate(
            relate_key=F("user_relate_type__relate_key"),
            relate_type_name=F("user_relate_type__relate_name"),
            user_name=F("user__user_name"),
            user_phone=F("user__phone"),
            full_name=F("user__full_name"),
            nickname=F("user__nickname"),
            with_user_name=F("with_user__user_name"),
            with_user_phone=F("with_user__phone"),
            with_full_name=F("with_user__full_name"),
            with_nickname=F("with_user__nickname")
        ).filter(with_user_id=user_id)

        # if not select_all:
        relate_user_obj = relate_user_obj.filter(user_relate_type__relate_key=relate_key)

        # 如果是查询间接邀请，则获取出直接邀请的用户
        if not direct_invite and not select_all:
            direct_inviter_users = list(UserRelateToUser.objects.filter(
                with_user_id=user_id, user_relate_type__relate_key="invite"
            ).values("user_id").distinct().order_by("user_id"))

            direct_inviter_users = [i["user_id"] for i in direct_inviter_users]
            relate_user_obj = relate_user_obj.exclude(user_id__in=direct_inviter_users)

        total = relate_user_obj.count()
        relate_user_list = list(relate_user_obj.values(
            "relate_key",
            "relate_type_name",
            "user_name",
            "user_phone",
            "full_name",
            "nickname",
            "with_user_name",
            "with_user_phone",
            "with_full_name",
            "with_nickname",
            "user_id",
            "with_user_id"
        ))
        # ------------------------- section 构建ORM end ------------------------------------

        # ------------------------- section 分页查询 start ------------------------------------
        try:
            page_list = Paginator(relate_user_list, size).page(page)
            page_list = page_list.object_list
        except EmptyPage as e:
            return {"page": page, "size": size, "total": total, "list": []}, None
        # ------------------------- section 分页查询 end   ------------------------------------
        data_map = {}
        EnrollStatisticsServices, err = dynamic_load_class(import_path="xj_enroll.service.enroll_statistics_services", class_name="EnrollStatisticsServices")
        if not err:
            data, err = EnrollStatisticsServices.every_one_total(params={"user_id_list": [i["user_id"] for i in page_list]}, need_Pagination=False)
            data_map = {i["user_id"]: i for i in data}

        user_detail_list, err = DetailInfoService.get_list_detail(user_id_list=[i["user_id"] for i in page_list], filter_fields=["user_id", "avatar", "real_name"])
        user_detail_list = user_detail_list if user_detail_list else []
        user_detail_map = {i["user_id"]: i for i in user_detail_list}
        for j in page_list:
            j["amount"] = float(data_map.get(j["user_id"], {}).get("amount_total", 0))
            j["order_total"] = float(data_map.get(j["user_id"], {}).get("count_total", 0))
            j["avatar"] = user_detail_map.get(j["user_id"], {}).get("avatar", [])
            j["real_name"] = user_detail_map.get(j["user_id"], {}).get("real_name", "")

        return {"page": page, "size": size, "total": total, "list": page_list}, None

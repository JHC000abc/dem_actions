# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: r_9657.py
@time: 2023/11/16 11:27
@desc:

"""
from sdk.utils.util_times import TimeProcess
from sdk.temp.temp_supports import IsSolution
from sdk.utils.util_encrtpt import EncryptProcess
from sdk.utils.util_bos import BosAkSk


class Solution(IsSolution):
    """

    """

    def __init__(self, **kwargs):
        super(Solution, self).__init__()
        self.__dict__.update({k: v for k, v in [
            i for i in locals().values() if isinstance(i, dict)][0].items()})
        self.time = TimeProcess()
        self.encrypt = EncryptProcess()
        self.bos = BosAkSk()

    def get_main_json(self):
        """

        """
        return {
            "info": {},
            "images": {}
        }

    def get_info(self):
        """

        """
        return {
            "description": "COCO 2023 Dataset",
            "version": "1.0",
            "year": int(self.time.get_normal_date("%Y")),
            "date_created": self.time.get_normal_date("%Y/%m/%d"),
        }

    def get_images(self, url_split, uuid, size):
        """

        """
        def __get_date_captured(name):
            _time = name.split(".")[0].split("_")[-2]
            y = _time[:4]
            m = _time[4:6]
            d = _time[6:8]
            h = _time[8:10]
            ms = _time[10:12]
            s = _time[12:]
            return "{}-{}-{} {}:{}:{}".format(y, m, d, h, ms, s)

        return {
            "file_name": url_split[-1],
            "height": size.get("height"),
            "width": size.get("width"),
            "date_captured": __get_date_captured(url_split[-1]),
            "camera_position": "Rearview_mirrors",
            "mode": "RGB" if "rgb" in url_split[-1].lower() else "IR",
            "scenario": "incabin",
            "id": uuid,
        }

    def get_annotations(self, uuid, url_split, bbox_body, bbox_lefthand, bbox_righthand, face_bbox, hair, hat, scarf, upper_clothing):
        """

        """
        return {
            "type": "incabin_body",
            "bbox_body": bbox_body,
            "bbox_lefthand": bbox_lefthand,
            "bbox_righthand": bbox_righthand,
            "face_bbox": face_bbox,
            "hair": hair,
            "hat": hat,
            "scarf": scarf,
            "upper_clothing": upper_clothing,
            "person_gender": 1 if url_split[-1].split("_")[1].lower() == "m" else 0,
            "person_age": int(url_split[-1].split("_")[2]),
            "id": "{}_{}".format(uuid, url_split[-1].split("_")[0]),
            "image_id": uuid
        }

    def process(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        in_path = kwargs["in_path"]
        save_path = kwargs["save_path"]
        self.folder.create_folder(save_path)
        for file, name in self.get_file(in_path, status=True):
            # print(file, name)
            for args in self.read_line(file, _id=2):
                # print(args)
                # if args["num"]>80:
                url_list = self.json.loads(args["line"][args["headers"].index("url")])
                # print(len(url_list))
                # answer_str = self.get_answer(args, ["验收答案", "拟合答案","审核答案", "质检答案", "终审答案"])
                answer_str = self.get_answer(args, ["验收答案", "审核答案", "质检答案", "终审答案","拟合答案"])
                try:
                    for answer_list in self.parse_answer(answer_str, "results"):
                        for url, answer in zip(url_list, answer_list):
                            # print(answer)
                            # break

                            size = answer["size"]
                            url_split = self.folder.split_path(url)
                            save_name = url_split[-1]
                            origin_folder = url_split[-3:-1]
                            origin_folder.insert(0, "origin")
                            save_file_folder = self.make_out_path(save_path, origin_folder)
                            save_file_origin = self.folder.merge_path([save_file_folder, save_name])
                            self.bos.download(url, save_file_origin)
                            uuid = self.encrypt.make_md5(save_file_origin)
                            images = self.get_images(url_split, uuid, size)

                            bbox_body = []
                            face_bbox = []
                            bbox_lefthand = []
                            bbox_righthand = []
                            hair = {}
                            hat = {}
                            scarf = {}
                            upper_clothing = {}

                            status = False

                            for element in answer["elements"]:
                                # print("element--->", url)
                                # print(element)
                                typeId = element["typeId"]
                                print("typeId", typeId)

                                points = self.get_points(element["points"], 2,format=True)
                                # print("points",points)
                                if typeId == "rect_1":
                                    bbox_body = points
                                elif typeId == "rect_2":
                                    face_bbox = points
                                elif typeId == "rect_4":
                                    status = True
                                    print("rect_4", self.bos.get_download_url(url))

                                elif typeId == "rect_3":
                                    attribute = element["attribute"]
                                    if attribute:
                                        if attribute.get("hand") == "1":
                                            bbox_righthand = points
                                        elif attribute.get("hand") == "0":
                                            bbox_lefthand = points
                                        elif attribute.get("hand") == "2":
                                            print("互动手")
                                        else:
                                            print("未知手势", url)
                                    else:
                                        print("没有手势分类")

                                elif typeId == "area_1":
                                    attribute = element["attribute"]
                                    if attribute:
                                        type = attribute.get("type1").lower()
                                        color = attribute.get("color").lower()
                                        seg = points
                                        hat["type"] = type
                                        if images["mode"] != "IR":
                                            hat["color"] = color
                                        else:
                                            hat["color"] = ""
                                        if hat.get("seg") is not None:
                                            hat["seg"].append(seg)
                                        else:
                                            hat["seg"] = [seg]

                                elif typeId == "area_2":
                                    attribute = element["attribute"]
                                    if attribute:
                                        type = attribute.get("hair").lower().replace("midian_femal", "midian_female")
                                        color = attribute.get("color").lower()
                                        seg = points
                                        hair["type"] = type
                                        if images["mode"] != "IR":
                                            hair["color"] = color
                                        else:
                                            hair["color"] = ""
                                        if hair.get("seg") is not None:
                                            hair["seg"].append(seg)
                                        else:
                                            hair["seg"] = [seg]

                                elif typeId == "area_3":
                                    attribute = element["attribute"]
                                    if attribute:
                                        type = attribute.get("type1").lower()
                                        color = attribute.get("color").lower()
                                        seg = points
                                        scarf["type"] = type
                                        if images["mode"] != "IR":
                                            scarf["color"] = color
                                        else:
                                            scarf["color"] = ""
                                        if scarf.get("seg") is not None:
                                            scarf["seg"].append(seg)
                                        else:
                                            scarf["seg"] = [seg]

                                elif typeId == "area_4":
                                    attribute = element["attribute"]
                                    if attribute:
                                        type = attribute.get("type1").lower()
                                        color = attribute.get("color").lower()
                                        seg = points
                                        upper_clothing["type"] = type
                                        if images["mode"] != "IR":
                                            upper_clothing["color"] = color
                                        else:
                                            upper_clothing["color"] = ""
                                        if upper_clothing.get("seg") is not None:
                                            upper_clothing["seg"].append(seg)
                                        else:
                                            upper_clothing["seg"] = [seg]
                            result = {}
                            if not status:
                                if hair != {} or hat != {} or scarf != {} or upper_clothing != {}:
                                    annotation = self.get_annotations(uuid, url_split, bbox_body, bbox_lefthand, bbox_righthand, face_bbox, hair, hat, scarf, upper_clothing)
                                    info = self.get_info()
                                    result["info"] = info
                                    result["annotation"] = annotation
                                    result["images"] = images
                                else:
                                    self.success_lis.append([url, "【area error】"])
                                    raise ValueError(f"【area error】\t{url} \nhair:{hair}\nhat:{hat}\nscarf:{scarf}\nupper_clothing:{upper_clothing}")


                            # print(url,result)
                            json_folder = url_split[-3:-1]
                            json_folder.insert(0, "json")
                            save_json_folder = self.make_out_path(save_path, json_folder)
                            save_file_json = self.folder.merge_path([save_json_folder, save_name.split(".")[0] + ".json"])

                            self.save_result(save_file_json, data=result)
                except Exception as e:
                    print(args["num"], e, e.__traceback__.tb_lineno)
                    print(args)
                    if "【area error】" not in str(e):
                        self.error_lis.append([str(args["num"]),str(e)])


            if self.error_lis:
                self.save_result(self.folder.merge_path([save_path,"error.txt"]),data=self.error_lis)
            if self.success_lis:
                self.save_result(self.folder.merge_path([save_path, "error2.txt"]), data=self.success_lis)



if __name__ == '__main__':
    in_path = R"D:\Desktop\1"
    save_path = R"D:\Desktop\2"
    e = Solution()
    e.process(in_path=in_path, save_path=save_path)

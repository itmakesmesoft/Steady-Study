import http from "@/util/http-commons";

export default class UserService {

    async checkEmailDuplicate(params) {
        return await http.get(`account/checkEmail/${params}`).then((data) => data.data);
    }

    async checkNickNameDuplicate(params) {
        return await http.get(`account/checkNickName/${params}`).then((data) => data.data);
    }

    async onSignUp(params) {
        return await http.post("account/signup", params).then((data) => data.data);
    }

}
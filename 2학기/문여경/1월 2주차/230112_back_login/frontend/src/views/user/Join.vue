
<!--
    가입하기는 기본적인 폼만 제공됩니다
    기능명세에 따라 개발을 진행하세요.
    Sub PJT I에서는 UX, 디자인 등을 포함하여 백엔드를 제외하여 개발합니다.
 -->
<template>
  <div class="user join wrapC">
    <h1>가입하기</h1>
    <div class="form-wrap">
      <div class="input-with-label">
        <input v-model="nickName" id="nickname" placeholder="닉네임을 입력하세요." type="text" />
        <label for="nickname">닉네임</label>
        <div class="error-text" v-if="error.nickName">{{error.nickName}}</div>
      </div>

      <div class="input-with-label">
        <input v-model="email" id="email" placeholder="이메일을 입력하세요." type="text" />
        <label for="email">이메일</label>
        <div class="error-text" v-if="error.email">{{error.email}}</div>
      </div>

      <div class="input-with-label">
        <input v-model="password" id="password" :type="passwordType" placeholder="비밀번호를 입력하세요." />
        <label for="password">비밀번호</label>
        <div class="error-text" v-if="error.password">{{error.password}}</div>
      </div>

      <div class="input-with-label">
        <input
          v-model="passwordConfirm"
          :type="passwordConfirmType"
          id="password-confirm"
          placeholder="비밀번호를 다시한번 입력하세요."
        />
        <label for="password-confirm">비밀번호 확인</label>
        <div class="error-text" v-if="error.passwordConfirm">{{error.passwordConfirm}}</div>
      </div>
    </div>

    <label>
      <input v-model="isTerm" type="checkbox" id="term" />
      <span>약관을 동의합니다.</span>
    </label>

    <span @click="termPopup=true">약관보기</span>

    <button class="btn-bottom" @click="onJoin">가입하기</button>
  </div>
</template>

<script>
import UserService from "@/service/UserService"
import PV from "password-validator";
import * as EmailValidator from "email-validator";
import { allowedNodeEnvironmentFlags } from "process";
import { userInfo } from "os";

export default {
  created() {
    this.userService = new UserService();

    this.passwordSchema
      .is()
      .min(8)
      .is()
      .max(100)
      .has()
      .digits()
      .has()
      .letters();
  },
  data: () => {
    return {
      
      email: "",
      password: "",
      passwordConfirm: "",
      nickName: "",
      isTerm: false,
      isLoading: false,
      error: {
        email: false,
        password: false,
        nickName: false,
        passwordConfirm: false,
        term: false
      },
      isSubmit: false,
      passwordType: "password",
      passwordConfirmType: "password",
      termPopup: false,
      passwordSchema: new PV(),
    };
  },
  methods: {
    onJoin() {

      if(this.error.nickName) {
        alert("닉네임을 확인해주세요.")
      } 

      if(this.error.email) {
        alert("이메일을 확인해주세요.");
        return;
      } 

      if(this.error.password) {
        alert("비밀번호를 확인해주세요.");
        return;
      }

      if(this.error.passwordConfirm) {
        alert("비밀번호를 확인해주세요.");
        return;
      }

      if(!this.error.nickName && !this.error.email && !this.error.password && !this.error.passwordConfirm) {
        const userInfo = {
          "nickName" : this.nickName,
          "email" : this.email,
          "password" : this.password,
        };
        this.userService.onSignUp(userInfo).then(data => {
          if(data.status) {
            alert("회원가입이 완료되었습니다.");
            this.$router.push("/");
          } else {
            alert("회원가입에 실패했습니다.");
          }
        });
      }
    },
    checkForm() {
      if (this.email.length >= 0 && !EmailValidator.validate(this.email))
        this.error.email = "이메일 형식이 아닙니다.";
      else this.error.email = false;

      if (
        this.password.length >= 0 &&
        !this.passwordSchema.validate(this.password)
      )
        this.error.password = "영문,숫자 포함 8 자리이상이어야 합니다.";
      else this.error.password = false;

      let isSubmit = true;
      Object.values(this.error).map(v => {
        if (v) isSubmit = false;
      });
      this.isSubmit = isSubmit;
    }
  },
  watch: {
    password: function(v) {
      this.checkForm();
    },
    email: function(v) {
      this.checkForm();

      if(!this.error.email) {
        this.userService.checkEmailDuplicate(this.email).then(data => {
          if(data.status === true) {
            this.error.email = false;
          } else {
            this.error.email = "중복 이메일입니다.";
          }
        });
      }
    },
    nickName: function() {
      if(this.nickName.trim().length >= 3) {
        this.userService.checkNickNameDuplicate(this.nickName).then(data => {
          if(data.status === true) {
            this.error.nickName = false;
          } else {
            this.error.nickName = "중복 닉네임입니다.";
          }
        })
      } else {
        this.error.nickName = "3글자 이상 입력해주세요.";
      }
    },
    passwordConfirm: function() {
      if(this.passwordConfirm !== this.password) {
        this.error.passwordConfirm = "패스워드가 일치하지 않습니다.";
      } else {
        this.error.passwordConfirm = false;
      }
    },
  },
};
</script>



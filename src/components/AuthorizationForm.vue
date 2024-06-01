<script>
import axios from 'axios';

export default{
    components: {
        axios
    },
    data() {
        return {
            show_password: false,
            user_info: {
                email: "",
                password: "",
            },
            rules: {
                emailMatch: v => func_required,
                // emailDontExist: v => /\S+@\S+\.\S+/.test(v) || "Почты не существует",
                // authFail: v => /\S+@\S+\.\S+/.test(v) || "Неверный логин или пароль",
            }
            
        }
    },
    methods: {
        authorization(){
            let a = axios.post(this.$store.state.root_url+ "/api/users/login/", this.user_info, {
                withCredentials: true,
                timeout: 5000 // Увеличьте тайм-аут до 5000 мс (5 секунд) или другого значения
            }).catch(error => {
                console.log(error);
            });
        },
        func_required(v) {
            this.required = !!v
            return this.required || "Требуется ввод"
        },
        func_emailMatch(v) {
            this.emailMatch = /\S+@\S+\.\S+/.test(v)
            return this.emailMatch || "Некорректная почта"
        },
    }

}
</script>

<template>
    <v-container fluid class="container">
        <v-form class="registration-form">
            <img src="" alt="" class="registration-logo"> 
            <h1 class="registration-title">
                Авторизация
                {{ $cookies.get("access_token") }}
            </h1>
            <hr class="registration-divider">
            <v-text-field 
                prepend-inner-icon="mdi-email-outline"
                v-model="this.user_info.email"
                type="email"
                class="registration-row-input" 
                label="Email"
                required 
            ></v-text-field>
            <v-text-field 
                :append-inner-icon="show_password ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show_password ? 'text' : 'password'"
                counter
                @click:append-inner="show_password = !show_password"
                prepend-inner-icon="mdi-lock-outline"
                class="registration-row-input" 
                label="Пароль" 
                required 
                v-model="this.user_info.password"
            ></v-text-field>
            <v-btn type="button" class="registration-submit" @click="authorization()" block>Авторизоваться</v-btn>
            <p class="register-signin">
                <pre>У вас нет аккаунта? <RouterLink class="register-signin-url" to="/register">Регистрация</RouterLink></pre>
            </p>
        </v-form>
    </v-container>
</template>

<style scoped>
</style>
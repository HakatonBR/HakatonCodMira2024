<script>
import axios from 'axios';

export default {
    components: {
        axios
    },
    data() {
        return {
            required: false,
            emailMatch: false,
            passwordMatch: false,
            passwordsEquals: false,

            show_password: false,
            user_info: {
                email: "",
                role: "",
                password: "",
                password_confirm: "",
            },
            items: [
                "HR менеджер",
                "Рекрутер",
                "Ресурсный менеджер"
            ],
            rules: {
                required: v => this.func_required(v),
                emailMatch: v => this.func_emailMatch(v),
                passwordMatch: v => this.func_passwordMatch(v),
                passwordsEquals: v => this.func_passwordsEquals(v),

                // emailExist: v => /\S+@\S+\.\S+/.test(v) || "Некорректная почта",
            }
        }
    },
    methods: {
        register(){
            let a = axios.post(this.$store.state.root_url+ `api/users/register/`, this.user_info, {
                timeout: 1000,
            }).catch(error => {
                console.log(error);
            });
            this.$router.push("/auth");
        },
        func_required(v) {
            this.required = !!v
            return this.required || "Требуется ввод"
        },
        func_emailMatch(v) {
            this.emailMatch = /\S+@\S+\.\S+/.test(v)
            return this.emailMatch || "Некорректная почта"
        },
        func_passwordMatch(v) {
            this.passwordMatch = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/.test(v)
            return this.passwordMatch || 'Пароль должен содержать хотя бы одну цифру, одну маленькую и одну большую букву, и быть длиннее 8 символов'
        },
        func_passwordsEquals(v) {
            this.passwordsEquals = v === this.user_info.password
            return this.passwordsEquals || 'Пароли не совпадают'
        },
    }
}
</script>

<template>
    <v-container fluid class="container">
        <v-form class="registration-form">
            <img src="" alt="" class="registration-logo"> 
            <h1 class="registration-title">
                Регистрация
            </h1>
            <hr class="registration-divider">
            <v-text-field 
                prepend-inner-icon="mdi-email-outline"
                v-model="this.user_info.email"
                type="email" 
                :rules="[rules.emailMatch]"
                class="registration-row-input" 
                label="Email"
                required 
            ></v-text-field>
            <v-select
                :prepend-inner-icon="'mdi-briefcase-outline'"
                v-model="this.user_info.role"
                :items="items"
                :rules="[rules.required]"
                label="Роль"
                required
                class="registration-row-input"
            ></v-select>
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
                :rules="[rules.passwordMatch]"
            ></v-text-field>
            <v-text-field 
                prepend-inner-icon="mdi-lock-outline"
                :type="show_password ? 'text' : 'password'"
                type="password" 
                class="registration-row-input" 
                label="Подтверждение пароля" 
                required 
                v-model="this.user_info.password_confirm"
                :rules="[rules.passwordsEquals]"
            ></v-text-field>
            <v-btn type="button" :disabled="!(required && emailMatch && passwordMatch && passwordsEquals)" class="registration-submit" @click="register()" block>Зарегистрироваться</v-btn>
            <p class="register-signin">
                <pre>Если у вас есть аккаунт <RouterLink class="register-signin-url" to="/auth">авторизация</RouterLink></pre>
            </p>
        </v-form>
    </v-container>
</template>

<style scoped>
</style>
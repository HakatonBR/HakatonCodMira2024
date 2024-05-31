<template>
    <v-card
      color="grey-lighten-4"
      rounded="0"
      flat
    >
      <v-toolbar density="compact">
        <v-toolbar-title>{{this.$store.state.logo_name}}</v-toolbar-title>
        <v-spacer/>
        <RouterLink to="../" ><v-btn>Главная</v-btn></RouterLink>
        <RouterLink to="/candidates"><v-btn>Кандидаты</v-btn></RouterLink>
        <RouterLink to="/vacancies"><v-btn>Вакансии</v-btn></RouterLink>
        <v-btn icon>
            <v-menu
                min-width="200px"
                rounded
            >
                <template v-slot:activator="{ props }">
                    <v-icon v-bind="props" icon="mdi-account-circle">
                    <span class="text-h5">{{ this.$store.state.user.initials }}</span>
                    </v-icon>
                </template>
                <v-card v-if="!this.$store.state.is_auth">
                    <v-card-text>
                        <div class="mx-auto text-center">
                            <RouterLink to="/register">Регистрация</RouterLink>
                            <v-divider class="my-3"></v-divider>
                            <RouterLink to="/auth">Авторизация</RouterLink>
                        </div>
                    </v-card-text>
                </v-card>
                <v-card v-else>
                    <v-card-text>
                        <div class="mx-auto text-center">
                            <h3>{{ this.$store.state.user.fullName }}</h3>
                            <p class="text-caption mt-1">
                                {{ this.$store.state.user.email }}
                            </p>
                            <v-divider class="my-3"></v-divider>
                            <RouterLink to="/reset_password" tag="button">Изменить пароль</RouterLink>
                            <v-divider class="my-3"></v-divider>

                            <!-- delete auth cookie -->
                            <RouterLink to="/" tag="button" @click="console.log('test')">Выход</RouterLink>
                        </div>
                    </v-card-text>
                </v-card>
            </v-menu>
        </v-btn>
      </v-toolbar>
    </v-card>
  </template>

<style scoped>
</style>

<script>
</script>
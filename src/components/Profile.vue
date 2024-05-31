<template>
    <v-container fluid>
        <h3>{{ id }}</h3>
    </v-container>
</template>

<style scoped>
</style>

<script>
export default {
    data: () => ({
      
    }),
    props: {
      id: {
        type: Number,
        required: true
      },
    }
  }
</script>
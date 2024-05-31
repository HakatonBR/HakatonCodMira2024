<template>
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-text-field
            v-model="filters.name"
            label="ФИО"
            @input="filterData"
          ></v-text-field>
          <v-text-field
            v-model="filters.age"
            label="Возраст"
            @input="filterData"
          ></v-text-field>
          <v-select
            v-model="filters.gender"
            :items="['Мужской', 'Женский']"
            label="Пол"
            @change="filterData"
          ></v-select>
          <v-text-field
            v-model="filters.experience"
            label="Стаж"
            @input="filterData"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-data-table
        :headers="headers"
        :items="filteredData"
        :items-per-page="itemsPerPage"
        :sort-by="sortBy"
        :sort-desc="sortDesc"
        @update:sort-by="updateSort"
        @update:sort-desc="updateSortDesc"
        @update:page="updatePage"
        @update:items-per-page="updateItemsPerPage"
      >
        <template v-slot:top>
          <v-toolbar flat>
            <v-toolbar-title>Таблица данных</v-toolbar-title>
            <v-divider class="mx-4" inset vertical></v-divider>
            <v-select
              v-model="itemsPerPage"
              :items="[5, 10, 25, 50]"
              label="Элементов на странице"
            ></v-select>
          </v-toolbar>
        </template>
      </v-data-table>
    </v-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        filters: {
          name: '',
          age: '',
          gender: '',
          experience: '',
        },
        headers: [
          { text: 'ФИО', value: 'name' },
          { text: 'Возраст', value: 'age' },
          { text: 'Пол', value: 'gender' },
          { text: 'Стаж', value: 'experience', sortable: true },
        ],
        items: this.generateItems(),
        filteredData: [],
        itemsPerPage: 5,
        sortBy: 'experience',
        sortDesc: false,
      };
    },
    methods: {
      generateItems() {
        const items = [];
        const names = ['Иванов Иван', 'Петров Петр', 'Сидорова Анна', 'Смирнова Мария', 'Кузнецов Алексей'];
        const genders = ['Мужской', 'Женский'];
  
        for (let i = 0; i < 100; i++) {
          const name = names[i % names.length];
          const age = 20 + (i % 30);
          const gender = genders[i % genders.length];
          const experience = i % 15;
  
          items.push({ name, age, gender, experience });
        }
  
        return items;
      },
      filterData() {
        this.filteredData = this.items.filter(item => {
          return (
            (this.filters.name === '' || item.name.includes(this.filters.name)) &&
            (this.filters.age === '' || item.age.toString().includes(this.filters.age)) &&
            (this.filters.gender === '' || item.gender === this.filters.gender) &&
            (this.filters.experience === '' || item.experience.toString().includes(this.filters.experience))
          );
        });
      },
      updateSort(sortBy) {
        this.sortBy = sortBy;
      },
      updateSortDesc(sortDesc) {
        this.sortDesc = sortDesc;
      },
      updatePage(page) {
        this.$refs.dataTable.page = page;
      },
      updateItemsPerPage(itemsPerPage) {
        this.itemsPerPage = itemsPerPage;
      },
    },
    created() {
      this.filterData();
    },
  };
  </script>
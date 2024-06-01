<template>
  <!-- Список сравниваемых кандидатов -->
  <v-navigation-drawer
        v-model="left_drawer"
        width="400"
        temporary
      >
    <v-btn icon="mdi-window-close" @click="left_drawer=false"/>
    <v-list>
      <v-list-item
        v-for="el in selected.sort((a, b) => a.id - b.id)"
        :key="el"
        :title="el.name"
        :subtitle="el.job"
        @click="switchRightDraw(el)"
      >
        {{el.id * 100}}%
        <Profile v-if="selected.length < 3" :id="el.id"/>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>

  <!-- Выбранный кандидат -->
  <v-navigation-drawer
    v-if="!!selectedCVinCompare"
    v-model="right_drawer"
    location="right"
    width="400"
    temporary
  >
    <v-btn icon="mdi-window-close" @click="right_drawer=false"/>
    <Profile :id="selectedCVinCompare.id"/>
  </v-navigation-drawer>

  <v-card>
    <!-- Поиск -->
    <template v-slot:text>
      <v-text-field
        v-model="search"
        label="Поиск"
        prepend-inner-icon="mdi-magnify"
        variant="outlined"
        hide-details
        single-line
      ></v-text-field>
    </template>
  <v-data-table
    v-model="selected"
    :headers="headers"
    :items="candidates"
    :search="search"
    :sort-by="[{ key: 'name', order: 'desc' }]"
    @click:row="gotoProfile"
    return-object
    show-select
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-dialog
          v-model="dialogUpload"
          max-width="500px"
        >
          <template v-slot:activator="{ props }">
            <v-btn
              class="mb-2"
              dark
              v-bind="props"
            >
              Загрузить резюме
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
            </v-card-title>
            <v-card-text>
              <v-file-input
                label="Выберите файл"
                counter
                show-size
                accept=".pdf,.docx,.rtf"
                @change="handleFileUpload"
              ></v-file-input>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <!-- редачить функции -->
              <v-btn
                variant="text"
                @click="closeUpload" 
              >
                Закрыть
              </v-btn>
              <v-btn
                variant="text"
                @click="upload"
              >
                Загрузить
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog
          v-model="dialogCreate"
          max-width="500px"
        >
          <template v-slot:activator="{ props }">
            <v-btn
              class="mb-2"
              dark
              v-bind="props"
            >
              Создать резюме
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
            </v-card-title>
            <v-card-text>
              <v-text-field
                v-model="editedItem.name"
                label="ФИО"
              ></v-text-field>
              <v-text-field
                v-model="editedItem.job"
                label="Должность"
              ></v-text-field>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                variant="text"
                @click="close"
              >
                Закрыть
              </v-btn>
              <v-btn
                variant="text"
                @click="save"
              >
                Сохранить
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-btn
          class="mb-2"
          dark
          @click="downloadCsv"
        >
          Выгрузить данные
        </v-btn>
        <v-btn 
          class="mb-2"
          dark
          @click.stop="switchLeftDraw()"
          :disabled="selected.length < 1"
        >
          Сравнить
        </v-btn>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="text-h5">Вы уверены, что хотите удалить этот элемент?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn variant="text" @click="closeDelete">Закрыть</v-btn>
              <v-btn variant="text" @click="deleteItemConfirm">Да</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:item.actions="{ item }">
      <v-icon
        size="small"
        @click.stop="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>
    <template v-slot:no-data>
      <v-btn @click="initialize">
        Перезагрузить
      </v-btn>
    </template>
  </v-data-table>
  </v-card>
</template>

<script>
import Profile from './Profile.vue'
  export default {
    components: {
      Profile
    },
    data: () => ({
      dialogCreate: false,
      dialogUpload: false,
      dialogDelete: false,
      headers: [
        { title: 'ID', key: 'id',align: 'start', sortable: false },
        { title: 'ФИО', key: 'name' },
        { title: 'Должность', key: 'job' },
        { title: 'Actions', key: 'actions', sortable: false },
      ],
      selected: [],
      right_drawer: false,
      left_drawer: false,
      candidates: [],
      editedIndex: -1,
      editedItem: {
        name: '',
        job: '',
      },
      defaultItem: {
        name: '',
        job: '',
      },
      search: '',
      selectedCVinCompare: null
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'Загрузить резюме' : 'Редактировать'
      }
    },

    watch: {
      dialogUpload (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },

    created () {
      this.initialize()
    },

    methods: {
      initialize () {
        this.candidates = [
        {
          "id": 1,
          "name": "Alice Johnson",
          "job": "Engineer"
        },
        {
          "id": 2,
          "name": "Bob Smith",
          "job": "Doctor"
        },
        {
          "id": 3,
          "name": "Charlie Brown",
          "job": "Teacher"
        },
        {
          "id": 4,
          "name": "David Wilson",
          "job": "Artist"
        },
        {
          "id": 5,
          "name": "Eva Davis",
          "job": "Lawyer"
        },
        {
          "id": 6,
          "name": "Frank Harris",
          "job": "Musician"
        },
        {
          "id": 7,
          "name": "Grace Lee",
          "job": "Scientist"
        },
        {
          "id": 8,
          "name": "Henry Walker",
          "job": "Writer"
        },
        {
          "id": 9,
          "name": "Ivy Hall",
          "job": "Nurse"
        },
        {
          "id": 10,
          "name": "Jack Young",
          "job": "Chef"
        },
        {
          "id": 11,
          "name": "Kara King",
          "job": "Designer"
        },
        {
          "id": 12,
          "name": "Liam Wright",
          "job": "Photographer"
        },
        {
          "id": 13,
          "name": "Mia Scott",
          "job": "Actor"
        },
        {
          "id": 14,
          "name": "Noah Green",
          "job": "Journalist"
        },
        {
          "id": 15,
          "name": "Olivia Adams",
          "job": "Architect"
        },
        {
          "id": 16,
          "name": "Paul Baker",
          "job": "Dentist"
        },
        {
          "id": 17,
          "name": "Quinn Rivera",
          "job": "Pharmacist"
        },
        {
          "id": 18,
          "name": "Ryan Perez",
          "job": "Pilot"
        },
        {
          "id": 19,
          "name": "Sara Roberts",
          "job": "Librarian"
        },
        {
          "id": 20,
          "name": "Tommy Clark",
          "job": "Mechanic"
        },
        {
          "id": 21,
          "name": "Uma Lewis",
          "job": "Veterinarian"
        },
        {
          "id": 22,
          "name": "Victor Robinson",
          "job": "Plumber"
        },
        {
          "id": 23,
          "name": "Wendy Martinez",
          "job": "Electrician"
        },
        {
          "id": 24,
          "name": "Xander Anderson",
          "job": "Technician"
        },
        {
          "id": 25,
          "name": "Yara Thomas",
          "job": "Therapist"
        },
        {
          "id": 26,
          "name": "Zachary Moore",
          "job": "Chemist"
        },
        {
          "id": 27,
          "name": "Amber White",
          "job": "Analyst"
        },
        {
          "id": 28,
          "name": "Brian Hill",
          "job": "Accountant"
        },
        {
          "id": 29,
          "name": "Claire Turner",
          "job": "Banker"
        },
        {
          "id": 30,
          "name": "Derek Allen",
          "job": "Broker"
        },
        {
          "id": 31,
          "name": "Emily Nelson",
          "job": "Consultant"
        },
        {
          "id": 32,
          "name": "Finn Carter",
          "job": "Chef"
        },
        {
          "id": 33,
          "name": "Gina Mitchell",
          "job": "Engineer"
        },
        {
          "id": 34,
          "name": "Hector Campbell",
          "job": "Firefighter"
        },
        {
          "id": 35,
          "name": "Isabella Roberts",
          "job": "Designer"
        },
        {
          "id": 36,
          "name": "Jake Simmons",
          "job": "Developer"
        },
        {
          "id": 37,
          "name": "Kylie Russell",
          "job": "Photographer"
        },
        {
          "id": 38,
          "name": "Leo Parker",
          "job": "Teacher"
        },
        {
          "id": 39,
          "name": "Mason Rivera",
          "job": "Doctor"
        },
        {
          "id": 40,
          "name": "Natalie Price",
          "job": "Lawyer"
        },
        {
          "id": 41,
          "name": "Oscar Torres",
          "job": "Musician"
        },
        {
          "id": 42,
          "name": "Penelope Watson",
          "job": "Nurse"
        },
        {
          "id": 43,
          "name": "Quincy Brooks",
          "job": "Scientist"
        },
        {
          "id": 44,
          "name": "Ruby Ward",
          "job": "Artist"
        },
        {
          "id": 45,
          "name": "Samuel Bell",
          "job": "Engineer"
        },
        {
          "id": 46,
          "name": "Tina Murphy",
          "job": "Journalist"
        },
        {
          "id": 47,
          "name": "Umar Gray",
          "job": "Writer"
        },
        {
          "id": 48,
          "name": "Vera Hughes",
          "job": "Actor"
        },
        {
          "id": 49,
          "name": "William Peterson",
          "job": "Architect"
        },
        {
          "id": 50,
          "name": "Xena Flores",
          "job": "Pilot"
        },
        {
          "id": 51,
          "name": "Yusuf Cox",
          "job": "Librarian"
        },
        {
          "id": 52,
          "name": "Zoe Diaz",
          "job": "Dentist"
        },
        {
          "id": 53,
          "name": "Adam Howard",
          "job": "Pharmacist"
        },
        {
          "id": 54,
          "name": "Bella Butler",
          "job": "Technician"
        },
        {
          "id": 55,
          "name": "Connor Foster",
          "job": "Therapist"
        },
        {
          "id": 56,
          "name": "Diana Bailey",
          "job": "Electrician"
        },
        {
          "id": 57,
          "name": "Ethan Rogers",
          "job": "Mechanic"
        },
        {
          "id": 58,
          "name": "Fiona Reed",
          "job": "Plumber"
        },
        {
          "id": 59,
          "name": "Gavin Morris",
          "job": "Veterinarian"
        },
        {
          "id": 60,
          "name": "Hannah Price",
          "job": "Analyst"
        },
        {
          "id": 61,
          "name": "Ian Bennett",
          "job": "Accountant"
        },
        {
          "id": 62,
          "name": "Jasmine Coleman",
          "job": "Banker"
        },
        {
          "id": 63,
          "name": "Kevin Barnes",
          "job": "Broker"
        },
        {
          "id": 64,
          "name": "Lydia Perry",
          "job": "Consultant"
        },
        {
          "id": 65,
          "name": "Mark Sanders",
          "job": "Chef"
        },
        {
          "id": 66,
          "name": "Nina Bryant",
          "job": "Engineer"
        },
        {
          "id": 67,
          "name": "Owen Hughes",
          "job": "Firefighter"
        },
        {
          "id": 68,
          "name": "Paula Richardson",
          "job": "Designer"
        },
        {
          "id": 69,
          "name": "Quentin Carter",
          "job": "Developer"
        },
        {
          "id": 70,
          "name": "Rita Bailey",
          "job": "Photographer"
        },
        {
          "id": 71,
          "name": "Steve Gray",
          "job": "Teacher"
        },
        {
          "id": 72,
          "name": "Tara Ellis",
          "job": "Doctor"
        },
        {
          "id": 73,
          "name": "Ulysses Lewis",
          "job": "Lawyer"
        },
        {
          "id": 74,
          "name": "Valerie Ramirez",
          "job": "Musician"
        },
        {
          "id": 75,
          "name": "Wayne James",
          "job": "Nurse"
        },
        {
          "id": 76,
          "name": "Xavier Russell",
          "job": "Scientist"
        },
        {
          "id": 77,
          "name": "Yvonne Bennett",
          "job": "Artist"
        },
        {
          "id": 78,
          "name": "Zane Cook",
          "job": "Engineer"
        },
        {
          "id": 79,
          "name": "Amelia Morgan",
          "job": "Journalist"
        },
        {
          "id": 80,
          "name": "Blake Mitchell",
          "job": "Writer"
        },
        {
          "id": 81,
          "name": "Chloe Watson",
          "job": "Actor"
        },
        {
          "id": 82,
          "name": "Daniel Jenkins",
          "job": "Architect"
        },
        {
          "id": 83,
          "name": "Erica Wood",
          "job": "Pilot"
        },
        {
          "id": 84,
          "name": "Felix Sanders",
          "job": "Librarian"
        },
        {
          "id": 85,
          "name": "Georgia Knight",
          "job": "Dentist"
        },
        {
          "id": 86,
          "name": "Harvey Bailey",
          "job": "Pharmacist"
        },
        {
          "id": 87,
          "name": "Isabel Martinez",
          "job": "Technician"
        },
        {
          "id": 88,
          "name": "Jacob Torres",
          "job": "Therapist"
        },
        {
          "id": 89,
          "name": "Kayla Robinson",
          "job": "Electrician"
        },
        {
          "id": 90,
          "name": "Logan Bell",
          "job": "Mechanic"
        },
        {
          "id": 91,
          "name": "Madison Brown",
          "job": "Plumber"
        },
        {
          "id": 92,
          "name": "Nolan Moore",
          "job": "Veterinarian"
        },
        {
          "id": 93,
          "name": "Olivia White",
          "job": "Analyst"
        },
        {
          "id": 94,
          "name": "Parker Davis",
          "job": "Accountant"
        },
        {
          "id": 95,
          "name": "Rachel Hill",
          "job": "Banker"
        },
        {
          "id": 96,
          "name": "Shawn Campbell",
          "job": "Broker"
        },
        {
          "id": 97,
          "name": "Taylor Adams",
          "job": "Consultant"
        },
        {
          "id": 98,
          "name": "Ursula Howard",
          "job": "Chef"
        },
        {
          "id": 99,
          "name": "Vince Baker",
          "job": "Engineer"
        },
        {
          "id": 100,
          "name": "Wendy Miller",
          "job": "Firefighter"
        }
        ]
      },

      deleteItem (item) {
        this.editedIndex = this.candidates.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true

        // TODO: delete item with id = item.id
      },

      deleteItemConfirm () {
        this.candidates.splice(this.editedIndex, 1)
        this.closeDelete()
      },

      close () {
        this.dialogCreate = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      closeDelete () {
        this.dialogDelete = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      closeUpload () {
        this.dialogUpload = false
        // some logic
      },

      save () {
        if (this.editedIndex > -1) {
          Object.assign(this.candidates[this.editedIndex], this.editedItem)
        } else {
          this.candidates.push(this.editedItem)
        }
        this.close()
      },

      upload () {
        // some logic
        this.closeUpload()
      },

      downloadCsv(){
        // some logic
      },

      gotoProfile(value, event){
        this.$router.push("/profile/" + event.item.id);
      },
      switchLeftDraw(){
        this.left_drawer = !this.left_drawer && (this.selected.length > 0)
        return this.left_drawer
      },

      switchRightDraw(el){
        console.log(!this.right_drawer && this.left_drawer)
        this.right_drawer = !this.right_drawer && this.left_drawer && (this.selected.length > 2)
        this.selectedCVinCompare = el
        return this.right_drawer
      },
    },
  }
</script>
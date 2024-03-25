<script setup>
	const route = useRoute()
</script>

<template>
	<MasterLayout>
		<div class="w-full h-full flex flex-col justify-center items-center">
            <div class="w-5/6 h-5/6">
                <ActionBar>
                    <template #header="headerProps">
                        <button @click="headerProps.revert_action" class="m-2 p-2 bg-slate-200 border-slate-300 border rounded-md hover:border-slate-500 hover:bg-slate-300 shadow-md active:bg-gray-400">Revert</button>
                        <button @click="headerProps.save_action" class="m-2 p-2 bg-slate-200 border-slate-300 border rounded-md hover:border-slate-500 hover:bg-slate-300 shadow-md active:bg-gray-400">Save</button>
                    </template>
                    <Card model="ProductCategory" :id="route.params.id" url="/master/product/category" padded controllable>
                        <template v-slot:header>
                        </template>
                        <template v-slot:button-box>
                        </template>
                        <template v-slot:main-info>
                            <CardGroup>
                                <CardField name="name" alias="Наименование" />
                            </CardGroup>
                        
                        </template>
                        <template v-slot:tabs>
                            <Tabs>
                                <Tab title="Основное">Основная информация</Tab>
                            </Tabs>
                        </template>
                    </Card>
                </ActionBar>
            </div>
        </div>
	</MasterLayout>
	
</template>

<script setup>
	const SuperCell = resolveComponent("SuperCell")
</script>

<template>
	<MasterLayout>
		<div class="p-5 w-full h-full">
            <ActionBar>
                <template #header="headerProps">
                    <NuxtLink to="/master/product/category/new" class="m-2 p-2 bg-slate-200 border-slate-300 border rounded-md hover:border-slate-500 hover:bg-slate-300 shadow-md active:bg-gray-400">Добавить</NuxtLink>
                    <button @click="headerProps.revert_action" class="m-2 p-2 bg-slate-200 border-slate-300 border rounded-md hover:border-slate-500 hover:bg-slate-300 shadow-md active:bg-gray-400">Отменить</button>
                    <button @click="headerProps.save_action" class="m-2 p-2 bg-slate-200 border-slate-300 border rounded-md hover:border-slate-500 hover:bg-slate-300 shadow-md active:bg-gray-400">Сохранить</button>
                </template>
                <List controllable clickable model="ProductCategory" url="/master/product/category/">
                    <Field name="name" alias="Наименование"/>
                </List>
            </ActionBar>
        </div>
	</MasterLayout>
	
</template>
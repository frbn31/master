<script setup>
	const SuperCell = resolveComponent("SuperCell")
</script>

<template>
	<MasterLayout>
		<div class="p-5 w-full h-full">
			<ActionBar>
				<template #header="headerProps">
					<button @click="headerProps.revert_action" class="m-2 p-2 bg-slate-200 border-slate-300 border rounded-md hover:border-slate-500 hover:bg-slate-300 shadow-md active:bg-gray-400">Отмена</button>
					<button @click="headerProps.save_action" class="m-2 p-2 bg-slate-200 border-slate-300 border rounded-md hover:border-slate-500 hover:bg-slate-300 shadow-md active:bg-gray-400">Сохранить</button>
				</template>
				<Card model="Product" padded creation url="/master/product/" controllable>
					<template v-slot:header>
					</template>
					<template v-slot:button-box>
					</template>
					<template v-slot:main-info>
						<CardGroup>
							<CardField name="name" alias="Наименование" />
							<CardField name="category_id" alias="Категория" />
						</CardGroup>
					</template>
					<template v-slot:tabs>
						<Tabs>
							<Tab title="Основное">Основная информация</Tab>
							<Tab title="Склад">Складская информация</Tab>
						</Tabs>
					</template>
				</Card>
			</ActionBar>
		</div>
	</MasterLayout>
	
</template>

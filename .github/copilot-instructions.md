# GitHub Copilot Instructions

You are helping with a Django + Nuxt 3 monorepo. Follow these rules:

## Frontend (Nuxt 3)

1. **ALWAYS reuse existing components** from `frontend/app/components/Ui/`
2. **NEVER create UI from scratch** - use Design System components:
   - UiButton (props: tipo, size, label)
   - UiInput (props: modelValue, placeholder, size)
   - UiEmpty (props: text, icon)
   - Quasar components (q-item, q-badge, q-scroll-area, etc.)

3. **New components MUST**:
   - Be reusable (props-driven, no hardcoded values)
   - Use Tailwind CSS for styling
   - Be responsive (use max-lg:, max-sm: modifiers)
   - Follow PascalCase naming

4. **Code structure**:
   ```vue
   <script setup>
   const props = defineProps({
     item: { type: Object, required: true }
   })
   const emit = defineEmits(['select'])
   </script>
   
   <template>
     <UiButton @click="emit('select')">
       {{ item.label }}
     </UiButton>
   </template>
   ```

## Backend (Django)

1. **ALWAYS follow app structure**:
   ```
   app_name/
   ├── admin/          # REQUIRED - subfolders
   ├── models/         # REQUIRED - subfolders
   ├── serializers/    # REQUIRED - subfolders
   └── viewsets/       # REQUIRED - subfolders
   ```

2. **Models MUST have**:
   - `verbose_name` on ALL fields
   - Proper Meta class with `verbose_name` and `verbose_name_plural`
   - `__str__` method

3. **Admin MUST have**:
   - `list_display`
   - `search_fields`
   - `list_filter`
   - Proper fieldsets

4. **ViewSets MUST have**:
   - `queryset`
   - `serializer_class`
   - `permission_classes` (ALWAYS defined)
   - Proper filter_backends if filterable

Example:
```python
# models/vaga.py
class Vaga(models.Model):
    titulo = models.CharField(
        verbose_name='Título',
        max_length=100,
    )
    
    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
    
    def __str__(self):
        return self.titulo

# admin/vaga_admin.py
@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'ativo']
    search_fields = ['titulo']
    list_filter = ['ativo']

# viewsets/vaga_viewsets.py
class VagaViewSet(NovadataModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer
    permission_classes = [AllowAny]  # or [IsAuthenticated]
```

## API Proxy

- Frontend requests to `/api/*` are proxied to Django backend
- Token added automatically via middleware
- NO need to handle authentication headers in frontend code

## Before Creating ANYTHING

1. Check if it already exists
2. Look at similar code in the project
3. Follow existing patterns EXACTLY
4. Maintain consistency over innovation

## File References

- See `.cursorrules` for detailed rules
- See `ARCHITECTURE.md` for architecture
- See `DESIGN_SYSTEM.md` for components
- See existing apps for examples (home/, recrutamento/)

## DON'T

- ❌ Create buttons/inputs without using Design System
- ❌ Put models outside models/ folder
- ❌ Create admin without proper configuration
- ❌ Create viewsets without permission_classes
- ❌ Hardcode values that should be props
- ❌ Ignore folder structure patterns

Remember: Consistency and reusability are CRITICAL in this project.
